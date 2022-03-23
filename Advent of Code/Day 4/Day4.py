import numpy as np

# Load Data
matrices = []
matrix = []
matrix_row = 1
with open('Advent of Code/Day 4/Input.txt') as textFile:
    for line in textFile:
        line = line.split()
        if not line: # skip blank lines
            continue
        elif len(line[0]) > 5: # first line
            called_numbers = line[0].split(',')
            continue
        elif matrix_row > 5: # prep a new matrix          
            matrices.append(matrix)
            matrix = []
            matrix_row = 1
        matrix.append(line)
        matrix_row += 1

matrices = np.array(matrices)
matrices = matrices.astype(np.int)

done = 0
for n in called_numbers:
    if done == 1: break
    # mark called numbers
    for i1, m in enumerate(matrices): # loop through matrices
        if done ==1: break
        for i2, r in enumerate(m): # loop through rows in matrix
            for i3, e in enumerate(r): # loop through numbers in row
                if int(e) == int(n):
                    matrices[i1][i2][i3] = -1
        # check if this matrix won horizontally
        for e in m.sum(axis=1):
            if e == -5:
                result = m
                last_number = n
                done = 1
        for e in m.sum(axis=0):
            if e == -5:
                result = m
                last_number = n
                done = 1

print(result)
print(last_number)