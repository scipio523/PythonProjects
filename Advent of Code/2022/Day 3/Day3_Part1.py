file = open('input.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]

    common_char = ''
    for c1 in firstpart:
        for c2 in secondpart:
            if c1 == c2:
                common_char = c1
                break
        if common_char != '': break

    if common_char.isupper():
        total += ord(c1) - 38
    else:
        total += ord(c1) - 96

print(total)