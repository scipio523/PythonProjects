file = open('input.txt', 'r')
lines = file.read().splitlines() 

groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
 
total = 0
for group in groups:
    common_char = ''
    for c0 in group[0]:
        if common_char: break
        for c1 in group[1]:
            if common_char: break
            for c2 in group[2]:
                if c0 == c1 == c2:
                    common_char = c0
                    break

    if common_char.isupper():
        total += ord(common_char) - 38
    else:
        total += ord(common_char) - 96

print(total)