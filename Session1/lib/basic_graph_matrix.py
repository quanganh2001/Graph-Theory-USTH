"""A naive pure python implementation of a Graph class

Based on ADJACENCY MATRIX

This implementation represents a graph where nodes are numbered, from 0 to N-1
where N is the order of the graph, known in advance.
Edges may be weighted by a float.

This implementation is for an DIRECTED GRAPH.

E. Viennet @ USTH, March 2024
"""


class Graph_Matrix:
    def __init__(self, n: int = 0):
        # use a list of list as a matrix (inefficient ! consider using numpy)
        self.adjacency_matrix = [[0.0 for _ in range(n)] for _ in range(n)]

    def _check_node_index(self, node):
        # checks if n is a valid node index in this graph
        if node < 0 or node >= len(self.adjacency_matrix):
            raise ValueError(f"invalid node index ({node})")

    def add_node(self, node: int):
        self._check_node_index(node)
        # nothing to do...

    def add_edge(self, node1, node2, weight=1.0, bidirectional=False):
        "Add edge from node1 to node2"
        self._check_node_index(node1)
        self._check_node_index(node2)
        self.adjacency_matrix[node1][node2] = weight
        if bidirectional:
            self.adjacency_matrix[node2][node1] = weight

    def get_nodes(self):
        return range(len(self.adjacency_matrix))

    def get_edges(self) -> list[tuple[int, int]]:
        """Returns the list of edges (from, to) with weight != 0.
        Weights are not returned.
        """
        edges = []
        n = len(self.adjacency_matrix)
        for node1 in range(n):
            for node2 in range(n):
                if self.adjacency_matrix[node1][node2] != 0.0:
                    edges.append((node1, node2))
        return edges

    def get_neighbors(self, node) -> list[int]:
        "List of node's neighbors (directed: node is the starting node)"
        self._check_node_index(node)
        row = self.adjacency_matrix[node]
        return [i for i, n in enumerate(row) if n != 0.0]

    def __repr__(self):
        return "\n".join(str(l) for l in self.adjacency_matrix)


if __name__ == "__main__":
    # Example usage
    g = Graph_Matrix(3)
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    print("Nodes:", g.get_nodes())
    print("Edges:", g.get_edges())
    print("Neighbors of 1:", g.get_neighbors(1))

    print(g)

"""
1. Compare the two implementations
    - Memory footprint
    - add_edge()
    - get_neighbors()
"""
