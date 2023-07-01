# A* pathfinding algorithm
from collections import deque
import random

def astar(start, end, graph):
    # Create a queue to store the nodes that we need to explore.
    queue = deque([start])

    # Create a set to store the nodes that we have already explored.
    explored = set()

    # Create a dictionary to store the cost of each node.
    #cost = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    #cost = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    cost = {'A': 0, 'B': random.randint(0, 1), 'C': random.randint(1, 2), 'D': random.randint(1, 3), 'E': random.randint(2, 4), 'F': random.randint(2, 5)}

    # While there are nodes in the queue:
    while queue:
        # Pop the next node from the queue.
        node = queue.popleft()

        # If the node is the goal, then we have found a path.
        if node == end:
            return cost[node]

        # Add the node to the explored set.
        explored.add(node)

        # For each neighbor of the node:
        for neighbor in graph[node]:
            # If the neighbor has not been explored, then add it to the queue.
            if neighbor not in explored:
                queue.append(neighbor)

            # Calculate the cost of the path from the start node to the neighbor.
            new_cost = cost[node] + graph[node][neighbor]

            # If the cost of the path to the neighbor is less than the cost that is currently stored in the dictionary, then update the dictionary.
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

    # If we reach this point, then there is no path from the start node to the goal node.
    return None

"""
# Create a graph.
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 3},
    'C': {'D': 4, 'E': 5},
    'D': {'E': 6},
    'E': {'F': 7}
}
"""

# Create a random graph.
graph = {
    'A': {'B': random.randint(0, 10), 'C': random.randint(0, 10)},
    'B': {'D': random.randint(0, 10)},
    'C': {'D': random.randint(0, 10), 'E': random.randint(0, 10)},
    'D': {'E': random.randint(0, 10)},
    'E': {'F': random.randint(0, 10)}
}


# Find the shortest path from node A to node F.
print(astar('A', 'F', graph))