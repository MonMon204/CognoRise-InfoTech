#
#    Task8_SudokoSolver.py
#
# Created on Fri Aug 23 2024 1:27:59 AM
#       Author: Mina Waguih
#
# Description: A simple Sudoku solver using backtracking
#



def is_valid(board, row, col, num):
    """
    Checks if it's possible to place a number in the given position.

    Args:
        board (list): The Sudoku board.
        row (int): The row index.
        col (int): The column index.
        num (int): The number to check.

    Returns:
        bool: True if the number can be placed, False otherwise.
    """
    # Check the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check the box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def solve_sudoku(board):
    """
    Solves the Sudoku puzzle using backtracking.

    Args:
        board (list): The Sudoku board.

    Returns:
        bool: True if the puzzle is solved, False otherwise.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True


def print_board(board):
    """
    Prints the Sudoku board.

    Args:
        board (list): The Sudoku board.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Example usage:
# board = [
#     [0, 9, 0, 5, 0, 0, 0, 0, 8],
#     [0, 3, 5, 0, 0, 0, 0, 0, 0],
#     [7, 0, 0, 0, 9, 0, 0, 0, 6],
#     [0, 0, 0, 0, 5, 0, 3, 0, 0],
#     [3, 0, 1, 7, 0, 0, 2, 0, 0],
#     [8, 0, 0, 0, 4, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 7, 0, 0, 0, 4],
#     [9, 0, 0, 0, 0, 2, 8, 0, 0]
# ]

print("************ Sudoku Solver ************")
print("Enter the Sudoku board (use 0 for empty cells):")

board = []

for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)


if solve_sudoku(board):
    print("\nSolution:\n")
    print_board(board)

else:
    print("No solution exists")