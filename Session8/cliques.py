import networkx as nx

def find_cliques_n(graph, n):
    cliques = [clique for clique in nx.find_cliques(graph) if len(clique) == n]
    return cliques

# Example usage
G = nx.Graph()
# Add edges to G (or generate a small random graph)
# For example:
# G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

n = 3  # Set the desired clique size
cliques_of_size_n = find_cliques_n(G, n)
print(f"All cliques of size {n}: {cliques_of_size_n}")

import time

# Generate a random graph with 20 nodes and probability of edge creation p=0.3
random_graph = nx.erdos_renyi_graph(20, 0.3)

# Test find_cliques_n function with different values of n
for n in range(2, 6):
    start_time = time.time()
    cliques_of_size_n = find_cliques_n(random_graph, n)
    elapsed_time = time.time() - start_time
    print(f"Time taken for n={n}: {elapsed_time:.6f} seconds")
    print(f"All cliques of size {n}: {cliques_of_size_n}\n")
