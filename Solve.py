def FindEmpty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col

    return None


def ValidInput(grid, pos, num):
    # Check row valid
    for i in grid[pos[0]]:
        if num == i:
            return False

    # Check column valid
    for row in grid:
        if row[pos[1]] == num:
            return False

    # Check box valid
    row = pos[0] // 3
    col = pos[1] // 3
    for i in range(row * 3, row * 3 + 3):  # walk through the row in a box
        for j in range(col * 3, col * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True


def Solve(grid):
    foundEmpty = FindEmpty(grid)
    if not foundEmpty:
        return True

    row = foundEmpty[0]
    col = foundEmpty[1]

    for num in range(1, 10):
        if ValidInput(grid, (row, col), num):
            grid[row][col] = num

            if Solve(grid):
                return True

        grid[row][col] = 0

    return False
