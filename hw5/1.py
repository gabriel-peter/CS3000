# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

def getTranspose(g):
    g_r = Graph(g.V)

    # Recur for all the vertices adjacent to this vertex
    for i in g.graph:
        for j in g.graph[i]:
            g_r.addEdge(j,i)
    return g_r

def DFS(node, graph):
	explored = defaultdict(int)
	discovery = {}
	finish = {}
	parent = {}
	parent[node] = None
	clock = 1

	def DFShelper(node, graph, clock):
		explored[node] = 1
		discovery[node] = clock
		clock += 1
		for v in graph[node]:
			if explored[v] == 0:
				parent[v] = node
				DFShelper(v, graph, clock)

		finish[node] = clock
		clock += 1
	
	DFShelper(node, graph, clock)

	return finish, parent
                

# Create a graph given in the above diagram
g = Graph(6)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)

g.addEdge(4, 1)
g.addEdge(4, 2)
g.addEdge(4, 3)
g.addEdge(4, 5)

g.addEdge(5, 1)
g.addEdge(5, 2)
g.addEdge(5, 3)
g.addEdge(5, 4)

# g=Graph(9)

# g.addEdge('e','g')
# g.addEdge('e','b')
# g.addEdge('e','c')
# g.addEdge('e','f')

# g.addEdge('a','e')
# g.addEdge('a','b')

# g.addEdge('b','c')

# g.addEdge('c','a')

# g.addEdge('d','a')
# g.addEdge('d','e')

# g.addEdge('f','c')

# g.addEdge('g','d')
# g.addEdge('g','h')

# g.addEdge('h','e')
# g.addEdge('h','i')

# g.addEdge('i','f')


# g = Graph(8)
# g.addEdge('a', 'b')
# g.addEdge('b', 'e')
# g.addEdge('b', 'c')
# g.addEdge('b', 'f')

# g.addEdge('c', 'g')
# g.addEdge('c', 'd')

# g.addEdge('d', 'h')
# g.addEdge('d', 'c')

# g.addEdge('e', 'a')
# g.addEdge('e', 'f')
# g.addEdge('f', 'g')
# g.addEdge('g', 'f')

# g.addEdge('h', 'g')

# def SCC(G):

rev = getTranspose(g)
finish, parent = DFS(1, rev.graph)
print(finish, parent)
c = 1
comp = {k:None for k in g.graph.keys()}
print(comp)
for u,x in sorted(finish.items(), key=lambda x:x[1], reverse=True):
	print(u)
	if comp[u] == None:
		_, S = DFS(u, g.graph) 
		print('S', S)
		for v in S.keys():
			comp[v] = c
		c +=1

print(comp)


# g = Graph(5)
# g.addEdge('a', 'b')
# g.addEdge('b', 'c')
# g.addEdge('c', 'd')
# g.addEdge('d', 'e')



