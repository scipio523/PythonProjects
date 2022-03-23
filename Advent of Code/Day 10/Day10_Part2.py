with open("Advent of Code/Day 10/Input.txt") as file:
    data = file.read().split("\n")

brackets = {'[':']', '(':')', '{':'}', '<':'>'}
points_lookup = {')':1, ']':2, '}':3, '>':4}
points_list = []
for line in data:
    expected = []
    points = 0
    corrupted = False
    for i, char in enumerate(line):
        if char in brackets: # left bracket
            expected.append(brackets[char])
        else: # right bracket
            if char == expected[-1]:
                expected.pop()
            else:
                corrupted = True
                break # skip corrupted lines
    if not corrupted and expected: # incomplete line
        for i in reversed(expected):
            points = points*5 + points_lookup[i]
        points_list.append(points)

points_list.sort()
result = points_list[int((len(points_list) - 1)/2)]
print(result)