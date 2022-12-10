# SudokuSolver
## Using this tool
By default it uses the [py-sudoku](https://pypi.org/project/py-sudoku/) library. It generates a random sudoku based on the difficulty set in line 9 in [Sudoku.py](https://github.com/DrTuup/SudokuSolver/blob/d967daa3eacbfa9b7672660d99ce4454a80f8634/Sudoku.py#L9).

## Setting up a custom sudoku
You can setup your own sudoku to be solved by setting the board variable in the function GenerateSudoku.py to your own in the following template:
`
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]
`
