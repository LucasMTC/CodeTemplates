from collections import defaultdict, deque

def create_graph(connections:list) -> dict:
    graph = defaultdict(list)
    for con in connections:
        start, end = con[0], con[1]
        graph[start].append(end)
    return graph

def find_indegree(graph:dict) -> dict:
    indegree = defaultdict(int)
    for list in graph.values():
        for node in list:
            indegree[node] += 1
    return indegree


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
    print(graph)
    indegree = find_indegree(graph)
    print(indegree)