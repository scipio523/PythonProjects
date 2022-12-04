vertices = [line.strip().split('-') for line in open('Advent of Code/Day 12/Test_Input.txt').readlines()]
graph = {}
for a, b in vertices: 
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
paths = [['start']]
count = 0
while paths:
    path = paths.pop()
    node = path[-1]            
    for n in graph[node]:
        if n == 'end':
            count += 1
            continue
        if n in path and n.islower(): 
            continue
        paths.append(path + [n])
print(count)