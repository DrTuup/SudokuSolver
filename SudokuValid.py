def RowValid(grid):
    for row in grid:
        for i in range(1, 10):
            if row.count(i) > 1:
                return False
    return True


def ColumnValid(grid, column):
    array = []
    for row in grid:
        if row[column] != 0:
            array.append(row[column])
        if len(array) != len(set(array)):
            return False

    return True


def SquareValid(grid):
    array = []
    for row in grid[0:2]:
        for pos in range(0, 3):
            if row[pos] != 0:
                array.append(row[pos])

    if len(array) != len(set(array)):
        return False

    array = []
    for row in grid[3:5]:
        for pos in range(3, 6):
            if row[pos] != 0:
                array.append(row[pos])

    if len(array) != len(set(array)):
        return False

    array = []
    for row in grid[6:8]:
        for pos in range(6, 9):
            if row[pos] != 0:
                array.append(row[pos])

    if len(array) != len(set(array)):
        return False

    return True


def PrintSudoku(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def IsValid(grid):
    if not RowValid(grid):
        return False
    for column in range(9):
        if not ColumnValid(grid, column):
            return False
    if not SquareValid(grid):
        return False

    return True
