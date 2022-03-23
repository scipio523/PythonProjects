vertices = [line.strip().split('-') for line in open('Advent of Code/Day 12/Input.txt').readlines()]
graph = {}
for a, b in vertices: 
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
n_visits = {node: 0 for node in graph}

def search(stack, node, n_paths):
    if n_visits[node] and node.islower(): # node has been visited before and is a lower case cave
        return n_paths
    if node == 'end':
        return n_paths + 1
    else:
        stack.append(node)
        n_visits[node] += 1
        for nb in graph[node]:
            n_paths = search(stack, nb, n_paths)
        stack.pop()
        n_visits[node] -= 1
    return n_paths

print(search([], 'start', 0))