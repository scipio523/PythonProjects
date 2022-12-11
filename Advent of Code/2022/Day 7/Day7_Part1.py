with open('input.txt', 'r') as file:
    lines = file.readlines()

fs = {} # filesystem
current_path = []

def update_cd(fs, current_path, name, size):
    if current_path[0] not in fs.keys():
        fs[current_path[0]] = dict()

    if len(current_path) > 1:
        fs[current_path[0]] = update_cd(fs[current_path[0]], current_path[1:], name, size)
    else:
        fs[current_path[0]][name] = size
    return fs

def get_data(data, current_path:list, name:str=None):
    if len(current_path) > 1:
        result = get_data(data[current_path[0]], current_path[1:], name)
    else:
        if name is None:
            result = list(data[current_path[0]].values())
        else:
            result = data[current_path[0]][name]
    return result

for line in lines:
    line = line.strip('\n')
    if line == '$ cd ..':
        current_path.pop()
    elif line[:4] == '$ cd':
        current_path.append(line[5:])
    elif line[:4] == '$ ls' or line[:3] == 'dir':
        continue
    else: # update the current dir
        size, name = line.split()
        fs = update_cd(fs, current_path, name, size)

print(fs)