import time
import numpy as np

start = time.time()

# Load Data
with open("Advent of Code/Day 7/Input.txt") as file:
    crabs = [int(x) for x in file.read().split(",")]

crabs = np.array(crabs)

min_cost = 99999999999
for i in range(crabs.max()):
    cost = abs(crabs - i).sum()
    if cost < min_cost: min_cost = cost

end = time.time()
print(min_cost)
print(f"Time: {end-start} seconds")