import numpy as np
grid = []

while True:
    try:
        user_defined_grid = int(input('choose a grid size\n>> '))
        break
    except ValueError as e:
        print('do try to enter only numbers please')
        continue

for r in range(user_defined_grid):
    row = []
    for c in range(user_defined_grid):
        row.append(0)
    grid.append(row)


def solve(grid, row, user_defined_grid):
    if row == user_defined_grid:
        return True

    for col in range(user_defined_grid):
        safe = True
        for prev_row in range(row):
            if grid[prev_row][col] == 'Q':
                safe = False
                break
        look_row = row - 1
        look_col = col - 1
        while look_row >= 0 and look_col >= 0:
            if grid[look_row][look_col] == 'Q':
                safe = False
                break

            look_row -= 1
            look_col -= 1

        look_row = row - 1
        look_col = col + 1
        while look_row >= 0 and look_col < user_defined_grid:
            if grid[look_row][look_col] == 'Q':
                safe = False
                break
            look_row -= 1
            look_col += 1

        if safe:
            grid[row][col] = 'Q'

            if solve(grid, row+1, user_defined_grid):
                return True
            grid[row][col] = 0


solve(grid, 0, user_defined_grid)
print(np.array(grid))
