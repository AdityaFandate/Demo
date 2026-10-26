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



from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def bfs(start, goal):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == goal:
                print("\nGoal node found!")
                return

            queue.extend(graph[node])

    print("\nGoal node not found!")


# Input
start = input("Enter start node: ")
goal = input("Enter goal node: ")

# Run BFS
bfs(start, goal)
