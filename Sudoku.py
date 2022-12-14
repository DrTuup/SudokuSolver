from SudokuValid import *
from Solve import *
import time
from sudoku import Sudoku


def GenerateSudoku():
    # generate a random sudoku
    board = Sudoku(3).difficulty(.3).board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                board[i][j] = 0

    return board


def main():
    # step zero, print the sudoku and start the timer
    print("Welcome to the sudoku solver, do you want to solve a custom sudoku or a random one?")
    print("1. Random Sudoku")
    print("2. Custom sudoku")
    choice = input("Enter your choice: ")
    if choice == "1":
        board = GenerateSudoku()
    elif choice == "2":
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    timer = time.time()
    print("This is the sudoku:")
    PrintSudoku(board)
    # first step, check if the sudoku is valid
    if not IsValid(board):
        return print("This is a not valid sudoku")
    while not Solve(board):
        Solve(board)
    print("\nThis is the solution:")
    PrintSudoku(board)
    print(f"\nThis took {time.time() - timer} seconds")


if __name__ == "__main__":
    main()
