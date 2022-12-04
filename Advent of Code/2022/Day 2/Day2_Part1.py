file = open('input.txt', 'r')
lines = file.readlines()
  
total = 0
for line in lines:
    their_choice = line.split()[0]
    my_choice = line.split()[1]

    if my_choice == 'X': total += 1
    elif my_choice == 'Y': total += 2
    elif my_choice == 'Z': total += 3

    if my_choice == 'X' and their_choice == 'A': total += 3
    elif my_choice == 'X' and their_choice == 'B': total += 0
    elif my_choice == 'X' and their_choice == 'C': total += 6

    elif my_choice == 'Y' and their_choice == 'A': total += 6
    elif my_choice == 'Y' and their_choice == 'B': total += 3
    elif my_choice == 'Y' and their_choice == 'C': total += 0

    elif my_choice == 'Z' and their_choice == 'A': total += 0
    elif my_choice == 'Z' and their_choice == 'B': total += 6
    elif my_choice == 'Z' and their_choice == 'C': total += 3

print(total)