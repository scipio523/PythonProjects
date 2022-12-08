# initialize lists
input = []
instructions = [[]]
crates = []
crate_stacks = []
procedure = []

# read input file
with open('input.txt', 'r') as file:
    for line in file:
        input.append(line)

# split instructions in half into drawing & procedure
delimiter = '\n'
for line in input:
    if line == delimiter:
        instructions.append([])
    elif line != delimiter: 
        instructions[-1].append(line.split('\n')[0])

# parse drawing into stacks of crates
drawing = instructions[0]
# parse row into crates
for line in drawing:
    crates.append([line[c * 4 + 1] for c in range(len(line) // 4 + 1)]) 
# transpose rows into columns (stacks)
crate_stacks = [list("".join(stack).strip()[::-1]) for stack in zip(*crates)]

# clean up steps into array
for step in instructions[1]:
    procedure.append([word for word in step.split(' ') if word.isdigit()])

for step in procedure:
    num_crates = int(step[0])
    from_stack = int(step[1])
    to_stack = int(step[2])

    crates = crate_stacks[from_stack-1][-num_crates:]
    del crate_stacks[from_stack-1][-num_crates:]

    for crate in crates:
        crate_stacks[to_stack-1].append(crate)

ans = [stack[-1] for stack in crate_stacks]
print(ans)