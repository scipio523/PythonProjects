vertices = [line.strip().split('-') for line in open('Advent of Code/Day 12/Test_Input.txt').readlines()]
graph = {}
for a, b in vertices: 
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

def search():
    node = 'start'
    path = [0, node] # path[0] added to track one revisit to small cave
    count = 0
    paths = [path]
    while len(paths) != 0:
        if node.islower() and path.count(node) > 1: # added for day 12B
            path[0] = 1
        for n in graph[node]:
            if n == 'start':
                continue
            if n == 'end':
                count += 1
                continue
            if n in path and n.islower() and path[0] == 1: # 'and path[0] == 1' added for day 12B 
                continue
            paths.append(path + [n])
        path = paths.pop()
        node = path[-1]
    return count
            
print(search())