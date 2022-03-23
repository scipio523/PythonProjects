from collections import Counter

# Load Data
with open("Advent of Code/Day 6/Input.txt") as file:
    fish = [int(x) for x in file.read().split(",")]

fish = Counter(fish)

for i in range(256):
    spawn = fish[0]
    for j in range(8):
        fish[j] = fish[j+1]
    fish[8] = spawn
    fish[6] += spawn

print(sum(fish.values()))