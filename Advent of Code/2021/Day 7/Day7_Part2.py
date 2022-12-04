import numpy as np

# Load Data
with open("Advent of Code/Day 7/Input.txt") as file:
    crabs = [int(x) for x in file.read().split(",")]

crabs = np.array(crabs)

min_cost = 99999999999
for i in range(crabs.max()):
    total_cost = 0
    for crab in crabs:
        cost = sum(range(abs(i - crab)+1))
        total_cost += cost
    if total_cost < min_cost: min_cost = total_cost

print(min_cost)