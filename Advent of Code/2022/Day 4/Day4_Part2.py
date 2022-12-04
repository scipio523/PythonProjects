file = open('input.txt', 'r')
lines = file.read().splitlines() 

count = 0
for pair in lines:
    first = pair.split(',')[0]
    second = pair.split(',')[1]
    
    if int(first.split('-')[1]) >= int(second.split('-')[0]) and int(second.split('-')[1]) >= int(first.split('-')[0]):
        count += 1

print(count)