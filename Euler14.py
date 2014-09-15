''' Project Euler problem 14 '''

powers = []
start = 2
while start < 1000000000000:
	powers.append(start)
	start=start*2

def collatz(n, count, search_list):
	
	if n in search_list:
		count += search_list.index(n)
		return n, count
	else:
		if n%2 == 0:
			n = n / 2
		else:
			n = 3*n + 1

		return collatz(n, count + 1, powers)

max_count = 0
max_i = 0
for i in range(2, 1000000):
	current = collatz(i, 0, powers)[1]
	if current > max_count:
		max_count = current
		max_i = i

print max_count, max_i
	
