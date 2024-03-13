import networkx as nx
import matplotlib.pyplot as plt
from hamilton import find_hamiltonian_circuit

# Create a random graph
G = nx.random_graphs.random_regular_graph(3, 6, seed=42)

# Find the Hamiltonian circuit
path = find_hamiltonian_circuit(G)

# Plot the graph and the Hamiltonian circuit
nx.draw(G, with_labels=True)
plt.title("Graph")
plt.show()

if path:
    print("Hamiltonian circuit:", path)
else:
    print("No Hamiltonian circuit exists")