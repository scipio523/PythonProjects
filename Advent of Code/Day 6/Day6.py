import numpy as np
import csv

# Load Data
with open('Advent of Code/Day 6/Input.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)[0]

data = map(int, data)
data = list(data)

for day in range(80):
    print(f'Day: {day+1}')
    new_fish = []
    for i, fish in enumerate(data):
        if fish == 0:
            data[i] = 6
            new_fish.append(8)
        else:
            data[i] -= 1
    for e in new_fish:
        data.append(e)

print(len(data))