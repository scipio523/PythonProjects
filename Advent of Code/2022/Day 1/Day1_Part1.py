file = open('input.txt', 'r')
lines = file.readlines()
  
max = 0
total = 0
for line in lines:
    if line == '\n':
        if total > max: max = total
        total = 0
    else:
        total += int(line)
print(max)
