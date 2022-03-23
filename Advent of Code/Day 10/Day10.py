with open("Advent of Code/Day 10/Input.txt") as file:
    data = file.read().split("\n")

# data = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

brackets = {'[':']', '(':')', '{':'}', '<':'>'}
points_lookup = {')':3, ']':57, '}':1197, '>':25137}
points = 0
expected = []
for line in data:
    for char in line:
        if char in brackets: # left bracket
            expected.append(brackets[char])
        else: # right bracket
            if char == expected[-1]:
                expected.pop()
            else:
                print(line, f"Expected {expected[-1]}, but found {char} instead.")
                points += points_lookup[char]
                break
print(points)