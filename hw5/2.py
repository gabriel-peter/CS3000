from collections import defaultdict

def FastTop(graph, weights):
    times = defaultdict(int)
    queue = []     #Initialize a queue
    in_deg = {k:0 for k in graph.keys()}

    def deleteNode(node, time_acc):
        # print('REMOVED NODE', node, 'TIME ACC', time_acc)
        times_acc = max(time_acc, times[node])    
        times[node] = time_acc
        for w in graph[node]:
            in_deg[w] -= 1
        for w in graph[node]:
            if in_deg[w] == -1: continue
            if in_deg[w] == 0:
                # queue.append(w)
                deleteNode(w, time_acc + weights[int(w)-1])
                in_deg[w] -= 1
            
        return time_acc

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
    while queue:
        u = queue.pop(0)
        deleteNode(u, weights[int(u)-1])

    return times
