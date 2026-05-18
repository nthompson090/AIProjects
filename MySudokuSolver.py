from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton
import sys

class SudokuGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sudoku Solver')
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.cells = [[QLineEdit(self) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j].setFixedSize(40, 40)
                self.cells[i][j].setMaxLength(1)
                self.cells[i][j].setAlignment(QtCore.Qt.AlignCenter)
                self.layout.addWidget(self.cells[i][j], i, j)
        self.solve_button = QPushButton('Solve', self) # Create a button to trigger the solving process
        self.solve_button.clicked.connect(self.solve_sudoku) # Connect the button's click event to the solve_sudoku method
        self.layout.addWidget(self.solve_button, 9, 0, 1, 9)
# Method to solve the Sudoku puzzle when the button is clicked
    def solve_sudoku(self):
        # Create a 2D list representing the Sudoku board, where empty cells are represented by 0
        board = [[0 if self.cells[i][j].text() == '' else int(self.cells[i][j].text()) for j in range(9)] for i in range(9)]
        if solve_sudoku(board):
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].setText(str(board[i][j]))
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No solution exists')
# Sudoku solving logic
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 11)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True
# Backtracking algorithm to solve the Sudoku puzzle
def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
# Function to find an empty cell in the Sudoku board
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SudokuGUI()
    ex.show()
    sys.exit(app.exec_())