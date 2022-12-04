template, rules = open('Advent of Code/Day 14/Test_Input.txt').read().split('\n\n')
rules = {y[0] : y[1] for y in [x.split(' -> ') for x in rules.splitlines()]}
pair_count = {key: template.count(key) for key in rules.keys()}
char_count = {x: template.count(x) for x in set(''.join(rules.values()))}

for i in range(40):
    new_pair_count = pair_count.copy()
    for k, v in pair_count.items():
        new_pair_count[k] -= v
        new_pair_count[k[0] + rules[k]] += v
        new_pair_count[rules[k] + k[1]] += v
        char_count[rules[k]] += v
    pair_count = new_pair_count
 
print(max(char_count.values()) - min(char_count.values()))