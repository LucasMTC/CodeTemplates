"""
Graph Depth First Search, as the name indicates, explores nodes as far as possible along each branch 
before backtracking. In other words, we go as deep as possible into a node's neighbors before visiting 
siblings. DFS is usually implemented using recursion or a stack. Graph DFS questions are common in 
interviews and often include questions like detecting cycles, connected components, or path existence.

Examples:
- Clone Graph: LeetCode 133
- Surrounded Regions: LeetCode 130

Time Complexity: O(V + E)  
Where V is the number of vertices and E is the number of edges in the graph  
Space Complexity: O(V) ## If input is considered as a hashmap of V + E, then space is also O(V + E)  
Where V is due to recursion stack or explicit stack storing vertices during traversal  
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

def dfs(graph:dict, start:str) -> list:
    ans = []
    stack = []
    stack.append(start)
    visited = set()
    visited.add(start)

    while stack:
        curr = stack.pop()
        ans.append(curr)
        for n in graph[curr]:
            if n not in visited:
                stack.append(n)
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
    print(dfs(graph, "A"))
    