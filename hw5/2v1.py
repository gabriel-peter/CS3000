from collections import defaultdict
import sys

def FastTop(graph, weights):
    labels = {k:0 for k in graph.keys()} # List for visited nodes.
    times = {k:0 for k in graph.keys()}
    queue = []     #Initialize a queue
    in_deg = {k:0 for k in graph.keys()}
    global count
    count = 0


    def deleteNode(node, time_acc):
        # print('REMOVED NODE', node, 'TIME ACC', time_acc)
        # print(times)
        # print(time_acc)
        global count
        count+=1
        labels[node] = count
        time_acc = max(time_acc, times[node])    
        times[node] = time_acc
        for w in graph[node]:
            # Track time additions here?
            times[w] = max(times[node], times[w])
            in_deg[w] -= 1
        for w in graph[node]:
            if in_deg[w] == 0:
                deleteNode(w, time_acc + weights[int(w)-1])
            
        # return time_acc

    # Marks all nodes
    for node in graph.keys():
        neighbors = graph[node]
        for out in neighbors:
            in_deg[out] += 1
        
    # Finds 0 in_degree nodes
    for node, deg in in_deg.items():
        if deg == 0:
            queue.append(node)

    #Queue starts.
    # print(queue)
    while queue:
        u = queue.pop(0)
        deleteNode(u, weights[int(u)-1])

        
    print(labels)
    return times


stdin = sys.stdin.readlines()
n = int(stdin[0])
edges = stdin[1:-1]
weights = [int(x) for x in stdin[-1].split(' ')]

# Graph construction
graph = defaultdict(list)
for u, edge in enumerate(edges):
    for l in edge.strip('\n').split(' '):
        l = int(l)
        if l == -1:
            graph[str(u+1)] = []
        else:
            graph[str(u+1)].append(str(l))

# Call Topological sort function and prints
times = FastTop(graph, weights)
for node in range(n):
    print(times[str(node+1)])