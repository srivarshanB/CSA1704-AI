def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_queens(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False
def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()
def solve_8_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]
    if solve_queens(board, 0):
        print("Solution found:")
        print_solution(board)
    else:
        print("No solution found.")
if __name__ == "__main__":
    solve_8_queens()
