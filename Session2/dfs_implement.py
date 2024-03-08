import networkx as nx
from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)
            neighbors = graph.neighbors(current_node)  # Assuming an undirected graph
            queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

# Example usage:
# Create a graph using NetworkX
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])

# Call BFS starting from node 1
bfs(G, 1)