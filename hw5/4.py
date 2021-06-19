from heapq import *
from collections import defaultdict

def dijkstra(edges, strat_node, end_node):
    g = defaultdict(list) 
    for start, end, weight in edges: 
        g[start].append((weight, end)) 
    q, visited = [(0, strat_node,())], set()
    while q:        
        (cost,v1,path) = heappop(q)
        if v1 not in visited:
            visited.add(v1)
            path = (v1, path)            
            if v1 == end_node:
                return (cost, path)
            for c, v2 in g.get(v1, ()):
                if v2 not in visited:
                    heappush(q, (cost+c, v2, path))
        print (q)   
    return float("inf")

if __name__ == "__main__":
    
    edges = [
        (1, 2, 8),
        (1, 3, 1),
        (1, 4, 9),
        (2, 5, 10),
        (3, 2, 12),
        (3, 5, 2),
        (3, 4, 7),
        (4, 5, 1),
        (5, 4, 3),
    ]

    for i in range(5):
        print(i+1)
        print (dijkstra(edges, 1, i+1))
        print()