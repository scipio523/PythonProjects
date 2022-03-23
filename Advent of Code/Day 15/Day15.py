import heapq

lines = open('Advent of Code/Day 15/Input.txt').read().splitlines()

# Using Dijkstra's algo
def part1():
    risk = [list(map(int, line)) for line in lines]
    paths = [(0, 0, 0)]
    visited = [[0] * len(row) for row in risk]

    while True:
        rf, x, y = heapq.heappop(paths)
        if visited[x][y]: continue
        if (x, y) == (len(risk) - 1, len(risk[x]) - 1): # at the end point
            return rf
        visited[x][y] = 1
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if not len(risk) > nx >= 0 <= ny < len(risk[0]): continue
            if visited[nx][ny]: continue
            heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))

def wrap(x):
    return (x - 1) % 9 + 1

def part2():
    _risk = [list(map(int, line)) for line in lines]
    risk = [[0] * len(row) * 5 for row in _risk * 5]
    r = len(_risk)
    c = len(_risk[0])

    for i in range(len(risk)):
        for j in range(len(risk[i])):
            risk[i][j] = wrap(_risk[i % r][j % c] + i // r + j // c)

    paths = [(0, 0, 0)]
    visited = [[0] * len(row) for row in risk]

    while True:
        rf, x, y = heapq.heappop(paths)
        if visited[x][y]: continue
        if (x, y) == (len(risk) - 1, len(risk[x]) - 1):
            return rf
        visited[x][y] = 1
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if not len(risk) > nx >= 0 <= ny < len(risk[0]): continue
            if visited[nx][ny]: continue
            heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))

print("Part 1:", part1())
print("Part 2:", part2())