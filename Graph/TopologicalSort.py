"""
This is an implementation of Topological Sorting using Kanh's Algorithm (BFS). Topological Sorting 
is a way of sorting that orders nodes based on their indegree values. In other words, for every 
connection from a node u -> v, u should always come before v in the sorted result. Topological 
Sorting questions are common for interviews and they normally take the form of something needing 
to happen before another thing.

Examples:
- Course Schedule: Leetcode 207
- Alien Dictionary: Leetcode 269

Time Complexity: O(V + E) 
Where V is the amount of vertices in the graph and E is the amount of edges in the graph.

Space Complexity: O(V)
Because we store every vertice in the graph in the output array.

Always remember that Topological Sorting only works on Directed Acyclical Graphs (DAGs).
"""

from collections import defaultdict, deque

def create_graph(connections:list) -> dict:
    graph = defaultdict(list)
    for con in connections:
        start, end = con
        graph[start].append(end)
        if end not in graph:
            graph[end] = []
    return graph

def find_indegree(graph:dict) -> dict:
    indegree = {node:0 for node in graph.keys()}
    for list in graph.values():
        for node in list:
            indegree[node] += 1
    return indegree

def topological_sort(graph:dict, indegree:dict) -> list:
    queue = deque()
    visited = set()
    ans = []
    for key, value in indegree.items():
        if value == 0:
            queue.append(key)
            visited.add(key)
    
    while queue:
        curr = queue.popleft()
        ans.append(curr)
        for node in graph[curr]:
            indegree[node] -= 1
            if node not in visited and indegree[node] == 0:
                queue.append(node)
                visited.add(node)
    return ans


if __name__ == "__main__":
    nodes = [
  ["A", "B"],
  ["A", "C"],
  ["B", "D"],
  ["C", "D"],
  ["C", "E"],
  ["D", "F"],
  ["E", "F"],
  ["E", "G"],
  ["F", "H"],
  ["G", "I"],
  ["H", "J"],
  ["I", "J"]
]
    graph = create_graph(nodes)
    indegree = find_indegree(graph)
    print(topological_sort(graph, indegree))