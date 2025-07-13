"""
Graph Breath First Search, as the name indicates, traverses every node in a connected graph 
level by level. In other words, we process a node and all of its neighbors closest to it before
moving on to the next level. Like in most BFS algorithms we use a queue to implement the 
traversal. Graph BFS questions are common in interviews and normally take the form of the 
shortest path from a starting node to another node.

Examples:
- Rotting Oranges: LeetCode 994
- Number of Islands: LeetCode 200

Time Complexity: O(V + E) 
Where V is the amount of vertices in the graph and E is the amount of edges in the graph
Space Complexity: O(V) ## IF the input is considered as a hashmap of V + E then the space is also O(V + E)
Where V is the amount of vertices in the graph because we add each of the vertices once to the queue
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

def bfs(graph:dict, start:str) -> list:
    ans = []
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)

    while queue:
        curr = queue.popleft()
        ans.append(curr)
        for n in graph[curr]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
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
    print(bfs(graph, "A"))