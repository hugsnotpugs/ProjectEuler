'''
Project Euler problem 18: 
Solved as a graph search problem using dijkstra's algorithm
to find the shortest path from each bottom starting point of the pyramid to the top
'''

string1 = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 9 70 98 73 93 38 53 60 04 23'''

from pqdict import PQDict
from graph_search import Graph

def dijkstra(graph, start):
    p_queue = PQDict()
    dist_to_start = {}
    prev_vert = {}

    # Fill the dictionaries with initial values
    for vert in graph:
        dist_to_start[vert] = 1000
        prev_vert[vert] = None

    # Initialize the priority queue dictionary
    dist_to_start[start] = 0
    for vert in graph:
        p_queue[vert] = dist_to_start[vert] # starts at 1000

    # BFS the priority queue dictionary
    while len(p_queue) > 0:
        current = p_queue.popitem()[0] # the first item in the tuple is the key
        neighbors = graph[current].keys()

        for vert in neighbors:
            neighbor_dist = graph[current][vert] 
            new_distance = dist_to_start[current] + neighbor_dist
            
            if new_distance < dist_to_start[vert]: # if smaller than the last dist_to_start replace
                p_queue[vert] = new_distance
                dist_to_start[vert] = new_distance
                prev_vert[vert] = current

    return prev_vert

# Convert the string to integers
rows = string1.split('\n')[1:]
for i in range(len(rows)):
	rows[i] = rows[i].split(' ')

	for j in range(len(rows[i])):
		rows[i][j] = int(rows[i][j])

# Create a graph that represents the integers
graph = Graph()
for i in range(len(rows)-1, -1, -1): # for each row in the pyramid
	for j in range(len(rows[i])): # for each item in the row
		graph.add_vert(str(i) + str(j))

# Initalize edges as the inverse of the node value (i.e. 70 --> 1/70)
for i in range(len(rows)-1, 0, -1):
	for j in range(len(rows[i])):
		if j == 0:
			graph.add_edge(str(i)+str(j), str(i-1)+str(j), 1/float((rows[i-1][j])))
		elif j == len(rows[i])-1:
			graph.add_edge(str(i)+str(j), str(i-1)+str(j-1), 1/float(rows[i-1][j-1]))
		else:
			graph.add_edge(str(i)+str(j), str(i-1)+str(j), 1/float(rows[i-1][j]))
			graph.add_edge(str(i)+str(j), str(i-1)+str(j-1), 1/float(rows[i-1][j-1]))

# Initialize all the different starting points into a list
starts = []
for key in graph.vertices:
	if key[:2] == '14':
		starts.append(key)

# Calculate the paths from each starting point
single_paths = []
for start in starts:
	path = dijkstra(graph.vertices, start)

	single_path = []
	def find_path(path, start):
		next = path[start]
		single_path.append(next)
		if next == None:
			return next
		else:
			return find_path(path, next)

	find_path(path, '00')
	single_paths.append(single_path)

# Create a dictionary mapping nodes to values
node_dict = {}
for i in range(len(rows)-1, -1, -1): 
	for j in range(len(rows[i])): 
		node_dict[str(i)+str(j)] = rows[i][j]

# Find highest sum
totals = []
for single_path in single_paths:
	total = 0
	for item in single_path:
		if item is not None:
			total += node_dict[item]
	total += 75
	totals.append(total)

# Highest sum:
print max(totals)
