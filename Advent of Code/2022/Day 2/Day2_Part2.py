file = open('input.txt', 'r')
lines = file.readlines()
  
total = 0
for line in lines:
    their_choice = line.split()[0]
    my_plan = line.split()[1]

    if my_plan == 'X': # lose
        if their_choice == 'A': my_choice = 'Z'
        elif their_choice == 'B': my_choice = 'X'
        elif their_choice == 'C': my_choice = 'Y'
        total += 0
    elif my_plan == 'Y': # draw
        if their_choice == 'A': my_choice = 'X'
        elif their_choice == 'B': my_choice = 'Y'
        elif their_choice == 'C': my_choice = 'Z'
        total += 3
    elif my_plan == 'Z': # win
        if their_choice == 'A': my_choice = 'Y'
        elif their_choice == 'B': my_choice = 'Z'
        elif their_choice == 'C': my_choice = 'X'
        total += 6

    if my_choice == 'X': total += 1
    elif my_choice == 'Y': total += 2
    elif my_choice == 'Z': total += 3

print(total)