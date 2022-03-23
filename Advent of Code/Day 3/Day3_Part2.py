# Load Data
file = open('Advent of Code/Day 4/Input.txt', 'r')
content = file.read()
l = content.split('\n')
file.close()

# oxygen generator rating
oxygen_list = l
for digit in range(len(oxygen_list[0])): # loop through each of the 12 "bits"
    
    ones_count = 0
    for number in range(len(oxygen_list)): # loop through each row to determine most common digit
        ones_count += int(oxygen_list[number][digit])   

    if ones_count >= len(oxygen_list)*0.5: # majority of digits are ones
        number_to_keep = 1
    else:
        number_to_keep = 0

    new_list = [i for i in oxygen_list if i[digit] == str(number_to_keep)] # create new list based on the chosen digit
    oxygen_list = new_list[:]

    if len(oxygen_list) == 1:
        oxygen_rating = oxygen_list[0]
        break

# CO2 scrubber rating
co2_list = l
for digit in range(len(co2_list[0])): # loop through each of the 12 "bits"
    
    ones_count = 0
    for number in range(len(co2_list)): # loop through each row to determine most common digit
        ones_count += int(co2_list[number][digit])   

    if ones_count >= len(co2_list)*0.5: # majority of digits are ones
        number_to_keep = 0
    else:
        number_to_keep = 1

    new_list = [i for i in co2_list if i[digit] == str(number_to_keep)] # create new list based on the chosen digit
    co2_list = new_list[:]

    if len(co2_list) == 1:
        co2_rating = co2_list[0]
        break

oxygen_rating = int(oxygen_rating, 2)
co2_rating = int(co2_rating, 2)

print(oxygen_rating*co2_rating)