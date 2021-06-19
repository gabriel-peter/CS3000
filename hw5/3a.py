from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.V = vertices # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


explored = defaultdict(int)
discovery = {}
finish = {}
parent = {}
parent['a'] = None
clock = 1

def DFS(node, graph):
    global clock
    explored[node] = 1
    discovery[node] = clock
    clock += 1
    for v in graph[node]:
        if explored[v] == 0:
            parent[v] = node
            DFS(v, graph)

    finish[node] = clock
    clock += 1


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

DFS('a', g.graph)
print(parent)
print('discovery', discovery)
print('finish', finish)

