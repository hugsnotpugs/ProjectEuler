''' Project euler problem 16: find the sum of the digits of 2^1000 
    Project euler problem 20: find the sum of the digits of 100! '''

import math

def sum_digits(number):
	digits = [int(i) for i in list(str(number))]
	return sum(digits)

print sum_digits(2**1000) # problem 16
print sum_digits(math.factorial(100)) # problem 20
