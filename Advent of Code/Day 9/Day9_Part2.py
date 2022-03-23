from functools import reduce

with open("Advent of Code/Day 9/Input.txt") as file:
    data = file.read().split("\n")
# data = ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']
grid = [[int(char) for char in row] for row in data]

def traverse(row, col):
    height = grid[row][col]
    if height == 9: return 
    grid[row][col] = 9 # don't check this point again    
    basin.append(height)
    traverse(row, max(col-1, 0))
    traverse(row, min(col+1, len(grid[0])-1))
    traverse(max(row-1, 0), col)
    traverse(min(row+1, len(grid)-1), col)

basin_list = []
for row in range(len(grid)):
    for col in range(len(grid[row])):
        basin = []
        traverse(row, col)
        if basin: basin_list.append(basin)

basin_sizes = [len(basin) for basin in basin_list]
basin_sizes.sort()
largest_basins = basin_sizes[-3:]
result = reduce((lambda x, y: x * y), largest_basins)
print(result)