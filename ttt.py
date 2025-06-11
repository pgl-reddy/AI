def print_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")
def check_win(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                    (0, 4, 8), (2, 4, 6)]  # Diagonals
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False
def check_draw(board):
    return all(cell != ' ' for cell in board)
def tic_tac_toe():
    board = [' ']*(9) # Empty board
    current_player = 'X'  # Player X starts
    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        board[move] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
tic_tac_toe()
