#
#    Task8_SudokoSolver.py
#
# Created on Fri Aug 23 2024 1:27:59 AM
#       Author: Mina Waguih
#
# Description:  This script is used to solve a Sudoku puzzle using backtracking algorithm.
#

import tkinter as tk
import tkinter.messagebox as messagebox

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


def solve_sudoku_gui():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = int(entry_list[i][j].get() or 0)
            row.append(value)
        board.append(row)

    def update_gui(board):
        for i in range(9):
            for j in range(9):
                if entry_list[i][j].get() == "0":
                    entry_list[i][j].config(fg="blue")
                entry_list[i][j].delete(0, tk.END)
                entry_list[i][j].insert(tk.END, str(board[i][j]))
        root.update_idletasks()
        root.update()

    def solve_sudoku(board):
        for j in range(9):
            for i in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            update_gui(board)
                            root.after(50)  # pause for 50ms
                            if solve_sudoku(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    if solve_sudoku(board):
        messagebox.showinfo("Solution Found", "The Sudoku puzzle has been solved.")
    else:
        messagebox.showinfo("No Solution", "No solution exists for the given Sudoku puzzle.")

def clear_board():
    """
    Clears the Sudoku board in the GUI.
    """
    for i in range(9):
        for j in range(9):
            entry_list[i][j].config(fg="black")
            entry_list[i][j].delete(0, tk.END)
            entry_list[i][j].insert(tk.END, "")


def move_to_next_entry(event):
    # Get the current entry box
    current_entry = root.focus_get()

    # Fill the current entry box with 0 if it's empty
    if current_entry.get() == "":
        current_entry.insert(tk.END, "0")

    # Move the cursor to the next entry box
    for i in range(9):
        for j in range(9):
            if entry_list[i][j] == current_entry:
                if i < 8:
                    entry_list[i + 1][j].focus_set()
                elif j < 8:
                    entry_list[0][j + 1].focus_set()
                return


# Create a welcome window
#welcome_window = tk.Toplevel(root)
root = tk.Tk()
root.title("Welcome")
root.geometry("600x250")

# Create a label with instructions
instructions_label = tk.Label(root, text="Welcome to Sudoku Solver!\n\nPlease enter the numbers in the Sudoku grid.\nUse 0 for empty cells.\n\nClick OK to continue.", font=("Arial", 14))
instructions_label.pack(padx=20, pady=20)

# Create an OK button to continue
ok_button = tk.Button(root, text="OK", command=root.destroy, font=("Arial", 14), bg="#4CAF50", fg="#fff", relief="flat")
ok_button.pack(pady=10)

# Wait for the welcome window to be closed before starting the main window
root.mainloop()

root = tk.Tk()
root.title("Sudoku Solver")

width = 400
height = 400
root.geometry("400x480")

# Create a frame for the Sudoku board
board_frame = tk.Frame(root)
board_frame.pack()

canvas = tk.Canvas(board_frame, width=width, height=height)
canvas.pack()

entry_list = []

for i in range(9):
    row = []
    for j in range(9):
        x0 = i * (width/9)
        y0 = j * (height/9)
        x1 = x0 + (width/9)
        y1 = y0 + (height/9)

        if (i + 1) % 3 == 0 and i != 8:
            canvas.create_line(x1, y0, x1, y1, width=3)
        else:
            canvas.create_line(x1, y0, x1, y1, width=1)

        if (j + 1) % 3 == 0 and j != 8:
            canvas.create_line(x0, y1, x1, y1, width=3)
        else:
            canvas.create_line(x0, y1, x1, y1, width=1)

        entry = tk.Entry(board_frame, width=2, font=("Arial", 18), justify="center", relief="flat", bg="#fff", highlightbackground="#ccc", highlightthickness=1)
        entry.place(x=x0+5, y=y0+5, width=(400/9)-10, height=(400/9)-10)
        row.append(entry)
    entry_list.append(row)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(padx=10, pady=10)

# Create the solve button
solve_button = tk.Button(button_frame, text="Solve", command=solve_sudoku_gui, font=("Arial", 14), bg="#4CAF50", fg="#fff", relief="flat")
solve_button.pack(side="left", padx=5, pady=5)

# Create the clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_board, font=("Arial", 14), bg="#e74c3c", fg="#fff", relief="flat")
clear_button.pack(side="left", padx=5, pady=5)

# Create the quit button
quit_button = tk.Button(button_frame, text="Quit", command=root.quit, font=("Arial", 14), bg="#ccc", fg="#333", relief="flat")
quit_button.pack(side="left", padx=5, pady=5)

# Bind the Enter key to move the cursor to the next entry box
root.bind("<Return>", move_to_next_entry)

    



root.mainloop()