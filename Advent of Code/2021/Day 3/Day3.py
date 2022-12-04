# Load Data
with open("'Advent of Code/Day 4/Input.txt") as file:
    data = [x for x in file.read().split("\n")]

ones_count = [0] * len(data[0])

for num in data:
    for i, digit in enumerate(num):
        ones_count[i] += int(digit)

gamma = ''
epsilon = ''
for i in ones_count:
    if i > 500: 
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)