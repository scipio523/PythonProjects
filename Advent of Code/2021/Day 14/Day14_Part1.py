from collections import Counter

data = [line.strip() for line in open('Advent of Code/Day 14/Input.txt').readlines()]
template = data[0]
rules = data[2:]
rules_dict = {}
for rule in rules:
    key, value = rule.split(' -> ')
    rules_dict[key] = value

steps = 40
for step in range(steps):
    print(step)
    new_template = ''
    for i in range(len(template)-1):
        new_template = new_template + template[i] + rules_dict[template[i:i+2]]
    new_template += template[-1]
    template = new_template

unique_chars = Counter(template)
max = unique_chars.most_common()[0][1]
min = unique_chars.most_common()[-1][1]
print(max - min)