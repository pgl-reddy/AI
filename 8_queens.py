def is_safe(board, current_row, current_col):
    for row in range(current_row):
        if board[row] == current_col or abs(board[row] - current_col) == current_row - row:
            return False
    return True

def backtrack(n, row, board, solution):
    if solution:  # If a solution is already found, stop further recursion
        return
    if row == n:
        solution.append(board.copy())
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            backtrack(n, row + 1, board, solution)
            board.pop()

n = int(input("Enter N: "))
solution = []
backtrack(n, 0, [], solution)

if solution:
    print("First Solution:", solution[0])
else:
    print("No solution found.")
