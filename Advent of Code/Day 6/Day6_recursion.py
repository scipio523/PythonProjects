import numpy as np
import csv

# Load Data
with open('Advent of Code/Day 6/Input.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)[0]

data = map(int, data)
data = list(data)

def count_fish(value, day, total_days):
    if day == total_days:
        return 1
    elif value == 0:
        return count_fish(6, day+1, total_days) + count_fish(8, day+1, total_days)
    else:
        return count_fish(value-1, day+1, total_days)

# 1421 is the answer for a single zero fish with 80 days
print(count_fish(0, 0, 80))