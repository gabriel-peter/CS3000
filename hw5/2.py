# Main algo method which returns mappings of
# min times needed to complete a node
def FastTop(graph, weights):
    times = {k:0 for k in graph.keys()}
    queue = []     #Initialize a queue
    in_deg = {k:0 for k in graph.keys()}

    # Removes a node and adjusts values that are
    # affected from its deletion (times, in_deg)
    def deleteNode(node, time_acc):
        time_acc = max(time_acc, times[node]
                    + weights[int(node)-1])    
        times[node] = time_acc
        for w in graph[node]:
            times[w] = max(times[node], times[w])
            in_deg[w] -= 1
        for w in graph[node]:
            if in_deg[w] == 0:
                deleteNode(w, time_acc)

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
        deleteNode(u, 0)

    return times