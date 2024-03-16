import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import community.community_louvain  # Louvain algorithm

# Load Facebook social circles dataset
# Replace 'path_to_file' with the actual path to the dataset file
path_to_file = "Session9/mini-project/facebook_combined.txt"
G = nx.read_edgelist(path_to_file)

# 1. Basic connectivity analysis
# Data description
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Is the graph connected (or how many connected components)?
if nx.is_connected(G):
    print("The graph is connected.")
else:
    print("Number of connected components:", nx.number_connected_components(G))

# Compute, plot and comment the distribution of nodes' degrees
degrees = [deg for node, deg in G.degree()]
degree_counts = Counter(degrees)
degree_hist = [degree_counts[deg] for deg in range(max(degrees) + 1)]

plt.figure(figsize=(10, 6))
plt.plot(degree_hist, 'b-', marker='o')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Are the graph(s) scale-free?
# A network is considered scale-free if its degree distribution follows a power-law distribution
# We can visually inspect the degree distribution plot and/or perform statistical tests for power-law distribution

# According to various centrality measures (betweenness, etc), which are the most important nodes?
# We'll compute and print the top 5 nodes based on betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)
sorted_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 nodes by betweenness centrality:")
for node, centrality in sorted_betweenness:
    print(f"Node {node}: {centrality}")

# 2. Find the communities using Louvain algorithm
# The Louvain algorithm detects communities in large networks efficiently
# It returns a partition, which is a dictionary where keys are nodes and values are community IDs
partition = community.community_louvain.best_partition(G)

# Visualize the communities
pos = nx.spring_layout(G)  # positions for all nodes
plt.figure(figsize=(10, 8))
cmap = plt.cm._colormaps['viridis']
nx.draw_networkx_nodes(G, pos, node_size=20, cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.title("Community Detection using Louvain Algorithm")
plt.axis("off")
plt.show()

# Describe quantitatively and qualitatively the communities
# We can analyze the size, density, and inter-community connections of the detected communities
community_sizes = Counter(partition.values())
print("\nCommunity sizes:", community_sizes)