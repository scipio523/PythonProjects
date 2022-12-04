# Load Data
with open("Advent of Code/Day 9/Input.txt") as file:
    grid = [x for x in file.read().split("\n")]

# test_data = [2199943210, 3987894921, 9856789892, 8767896789, 9899965678]
# grid = [str(x) for x in test_data]

min_points = []
for r, row in enumerate(grid):
    for c, point in enumerate(row):
        point = grid[r][c]
        if r == 0: # first row
            if c == 0: # top left corner
                if grid[r+1][c] > point and grid[r][c+1] > point:
                    min_points.append(int(point)+1)
            elif c == len(row)-1: # top right corner
                if grid[r+1][c] > point and grid[r][c-1] > point:
                    min_points.append(int(point)+1)
            else: # top row, not a corner
                if grid[r+1][c] > point and grid[r][c-1] > point and grid[r][c+1] > point:
                    min_points.append(int(point)+1)
        elif r == len(grid)-1: # bottom row
            if c == 0: # bottom left corner
                if grid[r-1][c] > point and grid[r][c+1] > point:
                    min_points.append(int(point)+1)
            elif c == len(row)-1: # bottom right corner
                if grid[r-1][c] > point and grid[r][c-1] > point:
                    min_points.append(int(point)+1)
            else: # bottom row, not a corner
                if grid[r-1][c] > point and grid[r][c-1] > point and grid[r][c+1] > point:
                    min_points.append(int(point)+1)
        elif c == 0: # first column, not a corner
            if grid[r-1][c] > point and grid[r][c+1] > point and grid[r+1][c] > point:
                min_points.append(int(point)+1)
        elif c == len(row)-1: # last column
            if grid[r-1][c] > point and grid[r][c-1] > point and grid[r+1][c] > point:
                min_points.append(int(point)+1)
        else: # inner point
            if grid[r+1][c] > point and grid[r-1][c] > point and grid[r][c+1] > point and grid[r][c-1] > point:
                min_points.append(int(point)+1)

print(sum(min_points))