"""Finding a Hamiltonian circuit in a given graph,
if it exists, based on a backtracking algorithm.

EV @ USTH, March 2023
"""

from typing import List, Optional  # for type hinting
import networkx as nx


def is_valid_vertex(graph: nx.Graph, v: int, pos: int, path: List[int]) -> bool:
    """Check if the current vertex v and last vertex in path are adjacent
    and if the vertex has already been included."""
    # Check if the current vertex and last vertex in path are adjacent
    if not graph.has_edge(path[pos - 1], v):
        return False
    # Check if the vertex has already been included in the path
    if v in path:
        return False
    return True


def hamiltonian_circuit_util(graph: nx.Graph, path: List[int], pos: int) -> bool:
    """Utility function to solve Hamiltonian Circuit problem using Backtracking."""
    # Base case: if all vertices are in the path and there is an edge from the last included vertex to the first vertex
    if pos == len(graph.nodes()) and graph.has_edge(path[pos - 1], path[0]):
        return True

    # Try different vertices as the next candidate in Hamiltonian Circuit
    for v in graph.nodes():
        if is_valid_vertex(graph, v, pos, path):
            path[pos] = v
            if hamiltonian_circuit_util(graph, path, pos + 1):
                return True
            # Remove current vertex if it doesn't lead to a solution
            path[pos] = -1

    return False


def find_hamiltonian_circuit(graph: nx.Graph) -> Optional[List[int]]:
    """Find the Hamiltonian circuit in the given graph if it exists."""
    path: List[int] = [-1] * len(graph.nodes())

    # Let vertex 0 be the first vertex in the path
    path[0] = list(graph.nodes())[0]

    if not hamiltonian_circuit_util(graph, path, 1):
        print("No Hamiltonian circuit exists")
        return None
    else:
        # Return to the starting point
        path.append(path[0])
        print("Hamiltonian circuit exists:\n", path)
        return path


if __name__ == "__main__":
    # Example usage
    G = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)])
    path = find_hamiltonian_circuit(G)
