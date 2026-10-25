def bfs(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

print("BFS Traversal:")
bfs(graph, "A")

# Cost / Complexity
# Time Complexity: O(V + E)
# Space Complexity: O(V)
