
def palindrome(integer):
	integer = str(integer)
	half = len(integer) // 2

	if len(integer)%2 == 0:
		left = integer[:half]
		right = integer[half:][::-1]	
	else:
		left = integer[:half+1]
		right = integer[half:][::-1]

	return True if left == right else False

total = 0
for i in range(1000000):
	binary = bin(i)[2:]
	if palindrome(i) and palindrome(binary):
		total += i

print total
