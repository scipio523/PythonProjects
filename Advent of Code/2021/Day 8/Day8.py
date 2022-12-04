import numpy as np

# Load Data
with open("Advent of Code/Day 8/Input.txt") as file:
    data = [x.split("|") for x in file.read().split("\n")]

count = 0
for i, line in enumerate(data):
    line[0] = sorted(line[0].split(" ")[:-1])
    line[1] = sorted(line[1].split(" ")[1:])

    decoder = {}
    for digit in line[0]: # first loop for 1, 4, 7, and 8
        digit = ''.join(sorted(digit))
        if len(digit) == 2:
            decoder[digit] = 1
        elif len(digit) == 4:
            decoder[digit] = 4
        elif len(digit) == 3:
            decoder[digit] = 7
        elif len(digit) == 7:
            decoder[digit] = 8

    for digit in line[1]:
        digit = ''.join(sorted(digit))
        if len(digit) in [2, 4, 3, 7]:
            number = decoder[digit]
            count += 1
        else:
            continue

print(count)