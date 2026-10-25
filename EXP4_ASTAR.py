
from heapq import heappush, heappop


def a_star(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        _, cost, node, path = heappop(queue)

        if cost > best_cost.get(node, float("inf")):
            continue

        if node == goal:
            return path, cost

        for neighbour, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                priority = new_cost + heuristic[neighbour]

                heappush(
                    queue,
                    (priority, new_cost, neighbour, path + [neighbour])
                )

    return None, None


graph = {
    "A": [("B", 4), ("C", 3)],
    "B": [("D", 5), ("E", 12)],
    "C": [("E", 10)],
    "D": [("F", 5)],
    "E": [("F", 4)],
    "F": []
}

heuristic = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 3,
    "E": 2,
    "F": 0
}

path, cost = a_star(graph, heuristic, "A", "F")

if path:
    print("Least-cost path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found")
