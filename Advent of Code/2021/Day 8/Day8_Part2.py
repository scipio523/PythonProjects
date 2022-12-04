# Load Data
with open("Advent of Code/Day 8/Input.txt") as file:
    data = [x.split("|") for x in file.read().split("\n")]

output = []
for line in data:
    line[0] = line[0].split()
    line[1] = line[1].split()

    decoder = {}
    for digit in line[0]: # first loop for 1, 4, 7, and 8
        digit = ''.join(sorted(digit))
        if len(digit) == 2:
            decoder[1] = digit
        elif len(digit) == 4:
            decoder[4] = digit
        elif len(digit) == 3:
            decoder[7] = digit
        elif len(digit) == 7:
            decoder[8] = digit
    
    decode_helper = decoder[4].replace(decoder[1][0], '') # this is a piece of the four
    decode_helper = decode_helper.replace(decoder[1][1], '')

    for digit in line[0]: # second loop for the remaining digits
        digit = ''.join(sorted(digit))
        if len(digit) == 5: # either 2, 3, or 5
            if decoder[1][0] in digit and decoder[1][1] in digit: # 3 is the only that has the 1 in it
                decoder[3] = digit
            elif decode_helper[0] in digit and decode_helper[1] in digit: # a 5 has this piece of the 4 but a 2 doesn't
                decoder[5] = digit
            else:
                decoder[2] = digit
        elif len(digit) == 6: # either 0, 6, or 9
            if decoder[1][0] not in digit or decoder[1][1] not in digit: # a 6 is the only one of the three that doesn't the 1 in it
                decoder[6] = digit
            elif decode_helper[0] in digit and decode_helper[1] in digit: # a 9 has this piece of the 4 but a 0 doesn't
                decoder[9] = digit
            else:
                decoder[0] = digit
    
    number = ''
    for digit in line[1]:
        digit = ''.join(sorted(digit))
        decoded_digit = [key for key, value in decoder.items() if value == digit][0]
        number += str(decoded_digit)
    output.append(int(number))

#print(output)
print(sum(output))