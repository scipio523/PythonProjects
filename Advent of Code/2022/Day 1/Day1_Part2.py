file = open('input.txt', 'r')
lines = file.readlines()
  
first = 0
second = 0
third = 0
total = 0
for line in lines:
    if line == '\n':
        if total > first: 
            third = second
            second = first
            first = total            
        elif total > second:
            third = second
            second = total
        elif total > third:
            third = total
        total = 0
    else:
        total += int(line)
        
print(first + second + third)
