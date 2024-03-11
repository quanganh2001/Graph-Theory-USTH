import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def searching_algo_BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Example graph data (replace with your own capacities)
graph_data = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 9, 14, 4],
    [3, -2, -5, -7, -8, -9],
    [2, -3, -4, -5, -6, -7],
    [-1, -2, -3, -4, -5, -6]
]

g = Graph(graph_data)
max_flow = g.ford_fulkerson(0, len(graph_data) - 1)
print(f"Max Flow: {max_flow}")

# Visualize the graph
G = nx.DiGraph()
for i in range(len(graph_data)):
    for j in range(len(graph_data[i])):
        if graph_data[i][j] > 0:
            G.add_edge(i, j, capacity=graph_data[i][j])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", width=1.5, edge_color="gray", arrows=True)
labels = nx.get_edge_attributes(G, "capacity")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

plt.title("Maximum Flow Visualization")
plt.show()