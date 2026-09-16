import matplotlib.pyplot as plt
import numpy as np

# 設置統一的學術圖表風格
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial'],
    'font.size': 12,
    'axes.spines.top': False,
    'axes.spines.right': False
})

def generate_figure_2_externalities():
    # 稍微加寬畫布，為外部圖例留出空間
    fig, ax = plt.subplots(figsize=(9, 6))
    q = np.linspace(0, 10, 100)
    
    mpb = 10 - q  # MSB = MPB
    mpc = 2 + q
    msc = 4 + q   # MEC = 2
    
    ax.plot(q, mpb, label='MSB = MPB', color='royalblue', linewidth=2.5)
    ax.plot(q, mpc, label='MPC', color='seagreen', linewidth=2.5)
    ax.plot(q, msc, label='MSC (MPC + MEC)', color='crimson', linewidth=2.5)
    
    # 標記均衡點
    ax.plot([4, 4], [0, 6], 'k--', alpha=0.5)
    ax.plot([0, 4], [6, 6], 'k--', alpha=0.5)
    ax.plot([3, 3], [0, 7], 'k--', alpha=0.5)
    
    # 填充 Deadweight Welfare Loss 陰影
    ax.fill([3, 4, 4], [7, 6, 8], color='gray', alpha=0.3, label='Deadweight Welfare Loss')
    
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 12)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # 添加箭頭與末端坐標軸標籤
    ax.plot(1, 0, transform=ax.transAxes, marker='>', markersize=8, color='black', clip_on=False)
    ax.plot(0, 1, transform=ax.transAxes, marker='^', markersize=8, color='black', clip_on=False)
    ax.text(1.02, 0, 'Quantity (Q)', transform=ax.transAxes, va='center', ha='left', fontweight='bold')
    ax.text(0, 1.04, 'Price / Costs / Benefits', transform=ax.transAxes, va='bottom', ha='center', fontweight='bold')
    
    # 使用數學下標與垂直錯位排版
    ax.text(3, -0.4, r'$Q_{social}$', ha='center', va='top', fontweight='bold', fontsize=13, clip_on=False)
    ax.plot([4, 4], [0, -1.0], 'k--', alpha=0.5, clip_on=False) 
    ax.text(4, -1.2, r'$Q_{market}$', ha='center', va='top', fontweight='bold', fontsize=13, clip_on=False)
    
    # --- 終極修復：圖例完全外置 ---
    # 將圖例放置在畫布的右側外部 (X=1.05)，徹底避免與曲線撞車
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', frameon=False)
    
    plt.tight_layout()
    # bbox_inches='tight' 會自動將外部圖例包裹進最終生成的 PNG 中
    plt.savefig('Figure_2_Externalities.png', dpi=300, bbox_inches='tight')
    plt.close(fig) # 釋放內存，防止重疊
    print("Generated Figure 2 successfully. (Legend completely externalized)")

def generate_figure_3_tech_ecosystem():
    fig, ax = plt.subplots(figsize=(9, 6))
    
    # 定義 Q 的範圍
    q = np.linspace(0.1, 10, 100)
    
    # 模擬數位服務市場：MC 較為平緩（符合軟體開發特性）
    ar = 10 - q          # AR (Demand)
    mr = 10 - 2 * q      # MR
    mc = 2 + 0.5 * q     # MC (Marginal Cost)
    
    ax.plot(q, ar, label='AR (Demand)', color='royalblue', linewidth=2.5)
    ax.plot(q, mr, label='MR', color='purple', linewidth=2.5)
    ax.plot(q, mc, label='MC (Marginal Cost)', color='crimson', linewidth=2.5)
    
    # 計算壟斷產量與價格 (MR = MC) -> 10 - 2q = 2 + 0.5q -> qm = 3.2, pm = 6.8
    qm = 3.2
    pm = 10 - qm
    mcm = 2 + 0.5 * qm
    
    # 計算完全競爭產量與價格 (MC = AR) -> 10 - q = 2 + 0.5q -> qc = 5.33, pc = 4.67
    qc = 5.33
    pc = 10 - qc
    
    # 繪製虛線
    ax.plot([qm, qm], [0, pm], 'k--', alpha=0.5)
    ax.plot([0, qm], [pm, pm], 'k--', alpha=0.5)
    ax.plot([qc, qc], [0, pc], 'k--', alpha=0.5)
    ax.plot([0, qc], [pc, pc], 'k--', alpha=0.5)
    
    # 填充 Welfare Loss 陰影 (修改圖例標籤以契合文本)
    ax.fill([qm, qm, qc], [pm, mcm, pc], color='orange', alpha=0.4, 
            label='Deadweight Loss\n(Reduced Consumer Surplus\n& Stifled Innovation)')
    
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 11)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # 添加箭頭與末端坐標軸標籤 (客製化 X 和 Y 軸標籤)
    ax.plot(1, 0, transform=ax.transAxes, marker='>', markersize=8, color='black', clip_on=False)
    ax.plot(0, 1, transform=ax.transAxes, marker='^', markersize=8, color='black', clip_on=False)
    ax.text(1.02, 0, 'Quantity of Digital Services (Q)', transform=ax.transAxes, va='center', ha='left', fontweight='bold')
    ax.text(0, 1.04, 'Price / Platform Fees (P)', transform=ax.transAxes, va='bottom', ha='center', fontweight='bold')
    
    # 完美避開 Y 軸碰撞的 LaTeX 數學標註
    ax.text(-0.3, pm, r'$P_m$', ha='right', va='center', fontweight='bold', fontsize=14, clip_on=False)
    ax.text(-0.3, pc, r'$P_c$', ha='right', va='center', fontweight='bold', fontsize=14, clip_on=False)
    ax.text(qm, -0.4, r'$Q_m$', ha='center', va='top', fontweight='bold', fontsize=14, clip_on=False)
    ax.text(qc, -0.4, r'$Q_c$', ha='center', va='top', fontweight='bold', fontsize=14, clip_on=False)
    
    # 核心亮點：加入緊扣 Section 4 文本的情境標註！
    ax.text(qm + 0.2, pm + 0.4, 'Exorbitant Fees\n(Platform Gatekeeping)', color='dimgray', fontsize=10, fontstyle='italic')
    
    # --- 終極修復：圖例完全外置 ---
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', frameon=False)
    
    plt.tight_layout()
    plt.savefig('Figure_3_Tech_Ecosystem.png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Generated Figure 3 (Tech Ecosystem) successfully. (Legend completely externalized)")

def generate_figure_4_nz_fishery():
    fig, ax = plt.subplots(figsize=(9, 5))
    years = np.arange(1975, 2011)
    
    biomass = [100, 95, 88, 80, 70, 60, 52, 45, 39, 34, 30, 28, 
               29, 32, 36, 42, 50, 58, 65, 72, 78, 83, 86, 88, 
               89, 90, 91, 91.5, 92, 92.5, 93, 93, 93.5, 94, 94, 94.5]
               
    ax.plot(years, biomass, color='teal', linewidth=3, marker='o', markevery=5, label='Fish Stock Biomass Index')
    ax.axvline(x=1986, color='crimson', linestyle='--', linewidth=2, label='Introduction of QMS (ITQs)')
    
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Biomass Index (1975 = 100)', fontweight='bold')
    ax.set_xlim(1975, 2010)
    ax.set_ylim(0, 110)
    
    # Figure 4 的曲線在右下角是空的，所以放裡面很安全
    ax.legend(loc='lower right', frameon=False)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('Figure_4_NZ_Fishery.png', dpi=300)
    plt.close(fig)
    print("Generated Figure 4 successfully.")

if __name__ == '__main__':
    generate_figure_2_externalities()
    generate_figure_3_tech_ecosystem()
    generate_figure_4_nz_fishery()
    print("All figures have been saved. Ready for publication.")