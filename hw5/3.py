from collections import defaultdict
import sys

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.V = vertices # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        print(stack[::-1]) # return list in reverse order
        return stack[::-1]

def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result

g = Graph(9)
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

# g.topologicalSort()
print(recursive_topological_sort(g.graph, 'a'))