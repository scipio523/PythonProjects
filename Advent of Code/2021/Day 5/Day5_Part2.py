import numpy as np

# Load Data
data = []
with open('Advent of Code/Day 5/Input.txt') as textFile:
    for line in textFile:
        line = line.split(' -> ')
        line[1] = line[1].rstrip('\n')
        line = [i.split(',') for i in line]
        line = [int(i) for e in line for i in e]
        data.append(line)

data = np.array(data)

#print(data.max(axis=0))
map = np.zeros((1000, 1000))

for line in data:
    
    x = line[0]
    y = line[1]
    while True:
        map[x][y] += 1
        if x == line[2] and y == line[3]: break
        if x < line[2]: x += 1
        elif x > line[2]: x -= 1
        if y < line[3]: y += 1
        elif y > line[3]: y -= 1
    
total = (map > 1).sum()
print(total)