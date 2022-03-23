import matplotlib.pyplot as plt
import numpy as np
data = [line.strip() for line in open('Advent of Code/Day 13/Input.txt').readlines()]
dots = []
folds = []
for i in data:
    if 'fold' in i:
        axis = i.split('=')[0][-1]
        point = i.split('=')[1]
        folds.append([axis, int(point)])
    elif not i:
        continue
    else:
        x = i.split(',')[0]
        y = i.split(',')[1]
        dots.append([int(x), int(y)])

for fold_axis, fold_point in folds:
    new_dots = []
    for dot in dots:
        x = dot[0]
        y = dot[1]
        if fold_axis == 'y': # horizontal line fold
            if y > fold_point:
                mirror = [x, fold_point*2 - y]
                if mirror not in dots:
                    new_dots.append(mirror)
            else:
                new_dots.append(dot)
        elif fold_axis == 'x': # vertical line fold
            if x > fold_point:
                mirror = [fold_point*2 - x, y]
                if mirror not in dots:
                    new_dots.append(mirror)
            else:
                new_dots.append(dot)
    dots = new_dots
new_dots.sort()
new_dots = np.array(new_dots)
x, y = new_dots.T
plt.scatter(x, -y)
plt.show()