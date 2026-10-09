# Board: 6 rows x 7 columns
# Empty slots use '0', players use 'X' and 'O'

ROWS = 6
COLS = 7
EMPTY = '0'

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    #Print the board to the console.
    col_numbers = ' '.join(str(i+1) for i in range(COLS))
    print("Columns:", col_numbers)
    for row in board:
        print(' '.join(row))
    print()

def is_valid_move(board, col):
    # Check if a move is valid (column in range and not full).
    if col < 0 or col >= COLS:
        return False
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    # Return the lowest open row in a given column, or None if full.
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None

def drop_piece(board, row, col, piece):
    #Place the piece into the board at (row, col).
    board[row][col] = piece

def winning_move(board, piece):
    # Check for a 4-in-a-row horizontally, vertically, or diagonally."""
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Diagonal (/)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    # Diagonal (\)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    return False

def is_draw(board):
    # Check if the board is full (draw).
    return all(board[0][c] != EMPTY for c in range(COLS))

def input_column(player):
    # Ask the player for a column number and parse it.
    try:
        s = input(f"Player {player} - Choose a column (1-{COLS}), or 'q' to quit: ").strip()
        if s.lower() == 'q':
            return 'q'
        col = int(s) - 1
        return col
    except ValueError:
        return None

def play_game():
    board = create_board()
    game_over = False
    turn = 0  # 0 -> X, 1 -> O
    pieces = ['X', 'O']

    print("Welcome to Connect Four!")
    print("Empty slots are '0'. Players are X and O. X goes first.")
    print_board(board)

    while not game_over:
        player_piece = pieces[turn % 2]
        col_input = input_column(player_piece)

        if col_input == 'q':
            print("Game exited.")
            return

        if col_input is None:
            print("Invalid input. Please enter a number between 1 and", COLS, "or 'q' to quit.")
            continue

        col = col_input
        if not is_valid_move(board, col):
            print("Invalid move (column full or out of range). Try again.")
            continue

        row = get_next_open_row(board, col)
        if row is None:
            print("This column is full. Choose another one.")
            continue

        drop_piece(board, row, col, player_piece)
        print_board(board)

        if winning_move(board, player_piece):
            print(f"Player {player_piece} wins! Congratulations!")
            game_over = True
            continue

        if is_draw(board):
            print("The board is full. It's a draw!")
            game_over = True
            continue

        turn += 1

play_game()
