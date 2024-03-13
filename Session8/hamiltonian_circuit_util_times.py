from hamilton import find_hamiltonian_circuit
import networkx as nx

call_count = 0 # Global variable to count the number of calls

# Example usage
G = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)])
call_count = 0  # Reset the call count
path = find_hamiltonian_circuit(G)
print("Number of calls to hamiltonian_circuit_util:", call_count)