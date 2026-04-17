#This is a tool which can add border around your image, showing the EXIF info & manufacturer logo

import os
from PIL import Image, ImageDraw, ImageFont, ExifTags


def extract_exif(img):
    """
    从图片中安全提取并格式化 EXIF 信息
    返回: (相机型号字符串, 拍摄参数字符串)
    """
    exif_data = {}

    # 尝试获取 EXIF 数据
    if hasattr(img, '_getexif') and img._getexif() is not None:
        info = img._getexif()
        for tag, value in info.items():
            decoded_tag = ExifTags.TAGS.get(tag, tag)
            exif_data[decoded_tag] = value

    # 1. 获取相机型号 (Model)
    camera_model = str(exif_data.get('Model', '')).strip()

    # 2. 获取焦段 (FocalLength)
    focal_length = exif_data.get('FocalLength')
    focal_str = ""
    if focal_length:
        try:
            # 处理 Pillow 中的 IFDRational 类型
            focal_str = f"{int(float(focal_length))}mm"
        except (ValueError, TypeError):
            pass

    # 3. 获取光圈 (FNumber)
    f_number = exif_data.get('FNumber')
    aperture_str = ""
    if f_number:
        try:
            aperture_str = f"f/{float(f_number):.1f}"
        except (ValueError, TypeError):
            pass

    # 4. 获取快门速度 (ExposureTime)
    exposure_time = exif_data.get('ExposureTime')
    shutter_str = ""
    if exposure_time:
        try:
            exp_val = float(exposure_time)
            if exp_val < 1.0:
                shutter_str = f"1/{int(1 / exp_val)}s"
            else:
                shutter_str = f"{exp_val}s"
        except (ValueError, TypeError, ZeroDivisionError):
            pass

    # 5. 获取 ISO (ISOSpeedRatings)
    iso = exif_data.get('ISOSpeedRatings')
    iso_str = f"ISO {iso}" if iso else ""

    # 将参数拼接在一起
    settings_list = [focal_str, aperture_str, shutter_str, iso_str]
    # 过滤掉空字符串，并用小圆点或空格隔开
    settings_str = " · ".join([s for s in settings_list if s])

    # 如果完全没有获取到信息，给个默认值（也可留空）
    if not camera_model and not settings_str:
        return "Unknown Camera", "No EXIF Data"

    return camera_model, settings_str


def process_photos_with_exif(input_folder, output_folder, font_path=None, logo_path=None, margin_ratio=0.035):
    """
    批量添加自适应 (4:3 或 3:4) 画廊白框、PNG商标，并无损保留原生数据
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.webp')):
            continue

        img_path = os.path.join(input_folder, filename)

        try:
            # 必须在转换为其他模式之前打开图片
            img = Image.open(img_path)

            # 抓取原图的底层 EXIF 和 ICC 色彩空间
            raw_exif = img.info.get('exif')
            icc_profile = img.info.get('icc_profile')

            # 提取要在画面上打印的文字信息
            camera_model, settings_str = extract_exif(img)

            # 统一转为 RGB 模式处理画面像素
            if img.mode != 'RGB':
                img = img.convert('RGB')

            w, h = img.size

            # 基础边距设定
            base_margin = int(max(w, h) * margin_ratio)
            w_with_margin = w + base_margin * 2
            top_margin = base_margin
            bottom_margin = int(base_margin * 1.8)
            h_with_margin = h + top_margin + bottom_margin

            # 【核心修改点 1】：自适应判断横图还是竖图
            if w >= h:
                target_ratio = 4 / 3  # 横版照片或正方形，使用 4:3 画布
            else:
                target_ratio = 3 / 4  # 竖版照片，使用 3:4 画布

            current_ratio = w_with_margin / h_with_margin

            if current_ratio > target_ratio:
                # 宽度占比太大，需要增加高度来凑目标比例
                new_w = w_with_margin
                new_h = int(w_with_margin / target_ratio)
            else:
                # 高度占比太大，需要增加宽度来凑目标比例
                new_h = h_with_margin
                new_w = int(h_with_margin * target_ratio)

            # 创建纯白底图
            background = Image.new('RGB', (new_w, new_h), 'white')

            # 计算图片居中偏上的位置
            offset_x = (new_w - w) // 2
            offset_y = (new_h - h) // 2 - int(base_margin * 0.3)

            background.paste(img, (offset_x, offset_y))

            # 利用 ImageDraw 在底部绘制 EXIF 文字
            draw = ImageDraw.Draw(background)

            # 【核心修改点 2】：使用画幅的“长边”来计算字号，保证横竖图的文字绝对大小一致
            # max(new_w, new_h) * 0.012 在 4:3 画幅下，正好等于之前 new_w * 0.016 的大小
            font_size = int(max(new_w, new_h) * 0.012)

            # 加载字体
            try:
                if font_path and os.path.exists(font_path):
                    font = ImageFont.truetype(font_path, font_size)
                else:
                    fallback_fonts = ["arial.ttf", "Helvetica.ttc", "SFNS.ttf", "simhei.ttf"]
                    font = None
                    for fb_font in fallback_fonts:
                        try:
                            font = ImageFont.truetype(fb_font, font_size)
                            break
                        except IOError:
                            continue
                    if not font:
                        font = ImageFont.load_default()
            except Exception as e:
                print(f"字体加载失败，使用默认极小字体。原因: {e}")
                font = ImageFont.load_default()

            text_color = (60, 60, 60)

            # 将文字固定在照片底部下方的一段距离
            text_y = offset_y + h + int(base_margin * 0.8)

            # 核心商标贴图逻辑
            text_x_left = offset_x

            if logo_path and os.path.exists(logo_path):
                try:
                    # 以 RGBA 模式打开商标，保留透明底
                    logo = Image.open(logo_path).convert("RGBA")

                    # 动态缩放 Logo 高度 (依然保持比文字稍高一点的比例)
                    target_logo_h = int(font_size * 1.4)
                    target_logo_w = int(logo.width * (target_logo_h / logo.height))

                    # 高质量抗锯齿缩放
                    logo = logo.resize((target_logo_w, target_logo_h), Image.Resampling.LANCZOS)

                    # 计算 Logo 坐标使其与文字垂直居中
                    logo_x = text_x_left
                    logo_y = text_y - (target_logo_h - font_size) // 2

                    # 贴上 Logo (第三个参数作 mask 处理透明度)
                    background.paste(logo, (logo_x, logo_y), logo)

                    # 将后面的相机型号文字向右推开，留出一定间距
                    text_x_left += target_logo_w + int(font_size * 0.8)
                except Exception as e:
                    print(f"⚠️ Logo 加载或处理失败，将跳过贴图: {e}")

            # 绘制相机型号 (在 Logo 右侧，或最左侧)
            draw.text((text_x_left, text_y), camera_model, font=font, fill=text_color)

            # 绘制拍摄参数 (居中偏右排版)
            settings_bbox = draw.textbbox((0, 0), settings_str, font=font)
            settings_width = settings_bbox[2] - settings_bbox[0]
            text_x_right = offset_x + w - settings_width
            draw.text((text_x_right, text_y), settings_str, font=font, fill=text_color)

            # 导出图片
            output_path = os.path.join(output_folder, filename)

            # 保存逻辑：将原生数据重新塞入新图片
            save_kwargs = {
                'quality': 95,
                'subsampling': 0
            }
            if raw_exif:
                save_kwargs['exif'] = raw_exif
            if icc_profile:
                save_kwargs['icc_profile'] = icc_profile

            background.save(output_path, **save_kwargs)

            print(
                f"✅ 成功: {filename} | 比例: {'4:3' if w >= h else '3:4'} | EXIF已继承 | {camera_model} | {settings_str}")

        except Exception as e:
            print(f"❌ 处理 {filename} 时发生错误: {e}")


# ================= Config. area =================

# 1. inputImageLocationPath
INPUT_DIR = "/Volumes/Example"

# 2. outputImagePath
OUTPUT_DIR = "/Volumes/Example"

# 3. macOS font path
FONT_FILE = "/System/Library/Fonts/Helvetica.ttc"

# 4. PNG logo path
LOGO_FILE = "/Volumes/Example/Canon_logo.png"

# Main process
process_photos_with_exif(INPUT_DIR, OUTPUT_DIR, font_path=FONT_FILE, logo_path=LOGO_FILE)
