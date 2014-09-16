''' Project euler problem 16: find the sum of the digits of 2^1000 '''

def sum_digits(number):
	digits = [int(i) for i in list(str(number))]
	return sum(digits)

print sum_digits(2**1000)
