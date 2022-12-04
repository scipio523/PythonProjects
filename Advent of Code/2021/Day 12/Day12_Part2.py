vertices = [line.strip().split('-') for line in open('Advent of Code/Day 12/Test_Input.txt').readlines()]
graph = {}
for a, b in vertices: 
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
n_visits = {node: 0 for node in graph}

def search(stack, node, n_paths, doubles_allowed):
    if n_visits[node] and node.islower():
        if not doubles_allowed or node == "start":
            return n_paths
        doubles_allowed = False
    if node == 'end':
        return n_paths + 1
    else:
        stack.append(node)
        n_visits[node] += 1
        for nb in graph[node]:
            n_paths = search(stack, nb, n_paths, doubles_allowed)
        stack.pop()
        n_visits[node] -= 1
        if n_visits[node] and node.islower():
            doubles_allowed = True
    return n_paths

print(search([], 'start', 0, False))
print(search([], 'start', 0, True))