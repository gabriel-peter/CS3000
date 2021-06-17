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

	# A function used by DFS
	def DFSUtil(self,v,visited):
		# Mark the current node as visited and print it
		visited[v]= True
		print(v, end=' ')
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited)


	def fillOrder(self,v,visited, stack):
		# Mark the current node as visited
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.fillOrder(i, visited, stack)
		stack.append(v)
	

	# Function that returns reverse (or transpose) of this graph
	def getTranspose(self):
		g = Graph(self.V)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g



	# The main function that finds and prints all strongly
	# connected components
	def printSCCs(self):
		
		stack = []
		# Mark all the vertices as not visited (For first DFS)
		visited =[False]*(self.V)
		# Fill vertices in stack according to their finishing
		# times
		for i in range(self.V):
			if visited[i]==False:
				self.fillOrder(i, visited, stack)

		# Create a reversed graph
		gr = self.getTranspose()
		
		# Mark all the vertices as not visited (For second DFS)
		visited =[False]*(self.V)

		# Now process all vertices in order defined by Stack
		while stack:
			i = stack.pop()
			if visited[i]==False:
				gr.DFSUtil(i, visited) # RECENT CHANGE
                # break
				print('')
                

# Create a graph given in the above diagram
# g = Graph(6)
# g.addEdge(1, 2)
# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(1, 5)

# g.addEdge(4, 1)
# g.addEdge(4, 2)
# g.addEdge(4, 3)
# g.addEdge(4, 5)

# g.addEdge(5, 1)
# g.addEdge(5, 2)
# g.addEdge(5, 3)
# g.addEdge(5, 4)

g=Graph(9)
g.addEdge('a','e')
g.addEdge('a','b')

g.addEdge('b','c')

g.addEdge('c','a')

g.addEdge('d','a')
g.addEdge('d','e')

g.addEdge('e','g')
g.addEdge('e','b')
g.addEdge('e','c')
g.addEdge('e','f')

g.addEdge('f','c')

g.addEdge('g','d')
g.addEdge('g','h')

g.addEdge('h','e')
g.addEdge('h','i')

g.addEdge('i','f')

print ("Following are strongly connected components " +
						"in given graph")
g.printSCCs()

