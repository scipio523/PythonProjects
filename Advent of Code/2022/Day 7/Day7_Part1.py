with open('input.txt', 'r') as file:
    lines = file.readlines()

fs = {} # filesystem
current_path = []

def update_cd(fs, current_path, name, size):
    if current_path[0] not in fs.keys():
        fs[current_path[0]] = dict()

    if len(current_path) == 1:
        fs[current_path[0]][name] = size
    else:
        fs[current_path[0]] = update_cd(fs[current_path[0]], current_path[1:], name, size)

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
        fs = update_cd(fs, current_path, name, int(size))

# print(fs)

dirs = []

def get_size(data:dict, path:list=[]):
    # print(path)
    size = 0
    # get list of content
    keys = data.keys()
    # iterate through list
    for k in keys:
        # if element is dict call self
        if isinstance(data[k], dict):
            size += get_size(data[k], path+[k])
        # else add to total size
        else:
            size += data[k]
    # add tuple of path and size to list of dirs
    dirs.append((path, size))
    return size

total_size = get_size(fs)

# part 1
score = 0
for d in dirs:
    if d[1] <= 100000:
        score += d[1] 
print(score)

# part 2
free_space = 70000000 - total_size
space_needed = 30000000 - free_space

possible_dirs = []
for d in dirs:
    if d[1] >= space_needed:
        possible_dirs.append(d)
possible_dirs.sort(key = lambda v: v[1])
# solution
path_to_smallest_possible_file = ''
for d in possible_dirs[0][0]:
    path_to_smallest_possible_file += f'{d}/'
path_to_smallest_possible_file = path_to_smallest_possible_file.rstrip('/')[1:]
print(possible_dirs[0][1])