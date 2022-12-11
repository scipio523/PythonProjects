def is_visible(grid:list, row:int, col:int):
    height = grid[row][col]
    visibility = 4 # assume visible from all 4 angles unless disproven

    for new_row in range(0, row):
        if grid[new_row][col] >= height: visibility -= 1; break
    for new_row in range(row+1, len(grid)):
        if grid[new_row][col] >= height: visibility -= 1; break
    for new_col in range(0, col):
        if grid[row][new_col] >= height: visibility -= 1; break
    for new_col in range(col+1, len(grid[0])):
        if grid[row][new_col] >= height: visibility -= 1; break
    
    if visibility == 0: return False
    else: return True

def scenic_score(grid:list, row:int, col:int):
    height = grid[row][col]
    up = 0; down = 0; left = 0; right = 0; 

    for new_row in reversed(range(row)):
        up += 1
        if grid[new_row][col] >= height: break
    for new_row in range(row+1, len(grid)):
        down += 1
        if grid[new_row][col] >= height: break
    for new_col in reversed(range(col)):
        left += 1
        if grid[row][new_col] >= height: break
    for new_col in range(col+1, len(grid[0])):
        right += 1
        if grid[row][new_col] >= height: break

    return up * down * left * right

def part_one(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_visible(grid, row, col):
                count += 1        
    return count

def part_two(grid):
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            res = max(res, scenic_score(grid, row, col))
    return res

def parse_data(path):
    with open(path, 'r') as file:
        return file.read().splitlines()

grid = parse_data('input.txt')

print('Part 1:', part_one(grid)) 
print('Part 2:', part_two(grid)) 