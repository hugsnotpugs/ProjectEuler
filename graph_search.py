''' Implementations of a graph class and a graph search class with BFS, DFS, Prim, Dijkstra methods '''

from pqdict import PQDict

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vert(self, keys=[]):
        if type(keys) == list or type(keys) == tuple:
            for key in keys:
                self.vertices[key] = {}
        else:
            self.vertices[keys] = {}

    def add_edge(self, from_key, to_key, weight=0):
            self.vertices[from_key][to_key] = weight
            self.vertices[to_key][from_key] = weight


class GraphSearch:

    def __init__(self, graph=None):
        self.graph = graph # GraphSearch requires a graph object

    def bfs(self, start, search=None):
        path = []
        queue = [start]

        while search not in path and len(queue) > 0:
            current = queue.pop(0)
            if current not in path:
                path += [current]
                queue += self.graph[current] # neighbors get added to queue

        if search in path:
            return True, path
        else:
            return False, path

    def dfs(self, start, search=None):
        path = []
        stack = [start]

        while search not in path and len(stack) > 0:
            current = stack.pop()
            if current not in path:
                path += [current]
                stack += self.graph[current]

        if search in path:
            return True, path
        else:
            return False, path

    def prim(self, start):
        p_queue = PQDict()
        prev_vert = {}
        key = {}

        for vert in self.graph:
            prev_vert[vert] = None
            key[vert] = 1000
        key[start] = 0

        for vert in self.graph:
            p_queue[vert] = key[vert]

        while p_queue:
            current = p_queue.popitem()[0]

            for vert in self.graph[current]:
                if vert in p_queue and self.graph[current][vert] < key[vert]:
                    prev_vert[vert] = current
                    key[vert] = graph[current][vert]
                    p_queue[vert] = graph[current][vert]

        return prev_vert

    def dijkstra(self, start):
        p_queue = PQDict()
        dist_to_start = {}
        prev_vert = {}

        # Fill the dictionaries with initial values
        for vert in self.graph:
            dist_to_start[vert] = 1000
            prev_vert[vert] = None

        # Initialize the priority queue dictionary
        dist_to_start[start] = 0
        for vert in self.graph:
            p_queue[vert] = dist_to_start[vert] # starts at 1000

        # BFS the priority queue dictionary
        while len(p_queue) > 0:
            current = p_queue.popitem()[0] # the first item in the tuple is the key
            neighbors = self.graph[current].keys()

            for vert in neighbors:
                neighbor_dist = self.graph[current][vert] 
                new_distance = dist_to_start[current] + neighbor_dist
                
                if new_distance < dist_to_start[vert]: # if smaller than the last dist_to_start replace
                    p_queue[vert] = new_distance
                    dist_to_start[vert] = new_distance
                    prev_vert[vert] = current

        return dist_to_start, prev_vert
