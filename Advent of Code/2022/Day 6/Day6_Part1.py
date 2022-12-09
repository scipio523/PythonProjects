with open('input.txt', 'r') as file:
    lines = file.readlines()

datastream = lines[0].strip()

from collections import Counter

for i, c in enumerate(datastream):
    if i >= 3:
        chunk = datastream[i-3:i+1]
        
        if len(chunk) == len(Counter(chunk)):
            print(i+1)
            break
        