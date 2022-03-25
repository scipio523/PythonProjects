# What is the least number of people where there is >50% chance that at least two of the people have the same birthday?

# Return the probability that at least two people have the same birthday given n people.
def birthday(n):
	result = 1.0
	days = 365.0
	for i in range(0, n):		
		result *= (days - i) / days		
	return (1-result)

print(birthday(23))