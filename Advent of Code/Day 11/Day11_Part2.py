import numpy as np

def valid_coordinate(grid, point):
    return 0 <= point[0] < grid.shape[0] and 0 <= point[1] < grid.shape[1]

def adjacent_cells(grid, point):
    surrounding_cells = np.array([np.subtract(point, (1, 1)), np.subtract(point, (-1, -1)), np.subtract(point, (1, -1)),
                                  np.subtract(point, (-1, 1)), np.subtract(point, (0, -1)), np.subtract(point, (0, 1)),
                                  np.subtract(point, (-1, 0)), np.subtract(point, (1, 0))])
    return list(filter(lambda x: valid_coordinate(grid, x), surrounding_cells))

def flash(grid, point):
    grid[point[0]][point[1]] = 11
    for p in adjacent_cells(grid, point):
        if grid[p[0]][p[1]] <= 9:
            grid[p[0]][p[1]] += 1
    return

def solve2():
    with open("Advent of Code/Day 11/Input.txt") as file:
        data = file.read().split("\n")
    grid = np.array([[int(i) for i in row] for row in data])

    flash_count = 0
    steps = 0
    while True:
        steps +=1
        grid += 1
        new_flashes = len(grid[grid == 10])
        
        while new_flashes > 0:
            # Increment the surrounding cells
            for point in np.argwhere(grid == 10):
                flash(grid, point)
            # Count the number of new flashes
            new_flashes = len(grid[grid == 10])
        # Reset all values >9 to 0
        flash_count += len(grid[grid > 9])
        grid[grid > 9] = 0

        if (grid == 0).sum() == grid.size:
            return steps

print( solve2() )