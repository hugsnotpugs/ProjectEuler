''' recursive method for small grids '''

def path(x_size, y_size):
	if x_size == 0 and y_size == 0:
		return 1

	paths = 0

	if x_size > 0:
		paths += path(x_size - 1, y_size)

	if y_size > 0:
		paths += path(x_size, y_size - 1)

	return paths

print path(20, 20)
