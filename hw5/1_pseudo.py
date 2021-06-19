#This class represents a directed graph using adjacency list representation
class Graph:
   
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
   
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[str(u)].append(str(v))
   
    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print (v, end=' ')
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i,visited)
  
    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited 
        visited[v] = True
        #Recur for all the vertices adjacent to this vertex
        print(visited)
        for i in self.graph[v]:
            if i not in visited.keys(): continue # BUG FIX IS IT A SCC?
            if not visited[i]:
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
        visited = {k:False for k in self.graph.keys()}
        # Fill vertices in stack according to their finishing
        # times
        for i in self.graph.keys():
            if not visited[i]:
                self.fillOrder(i, visited, stack)
  
        # Create a reversed graph
        gr = self.getTranspose()
           
        # Mark all the vertices as not visited (For second DFS)
        visited = {k:False for k in self.graph.keys()}
  
        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.DFSUtil(i, visited)
                print()