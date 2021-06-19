from collections import defaultdict
def findBrokers(graph):

	# Simplified DFS that only 
	# counts nodes visited: O(n+m)
	def DFS(node, graph):
		global count
		count = 0
		explored = defaultdict(int)

		def DFShelper(node, graph):
			global count
			explored[node] = 1
			count += 1
			for v in graph[node]:
				if explored[v] == 0:
					DFShelper(v, graph)

		
		DFShelper(node, graph)
		return count

	# Runs for each run node: O(n)
	for node in graph:
		influence_count = DFS(node, graph)
		if influence_count == len(graph):
			print(f'Node {node} is a powerbroker')




