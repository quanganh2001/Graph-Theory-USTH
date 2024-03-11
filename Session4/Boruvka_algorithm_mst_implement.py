import networkx as nx
import matplotlib.pyplot as plt
import random

def boruvka(graph):
    # Initialize a list to store the edges of the minimum spanning tree
    min_spanning_tree_edges = []
    
    while True:
        # Create a set for each component in the graph
        components = {node: {node} for node in graph.nodes}
        
        # Iterate over each edge and find the minimum-weight edge for each component
        for edge in graph.edges:
            u, v = edge
            component_u = next((comp for comp in components if u in components[comp]), None)
            component_v = next((comp for comp in components if v in components[comp]), None)

            # If the edge connects different components, add it to the minimum spanning tree
            if component_u != component_v:
                min_spanning_tree_edges.append(edge)
                # Merge the two components
                components[component_u].update(components[component_v])
                del components[component_v]

        # If there is only one component left, break the loop
        if len(components) == 1:
            break

    return min_spanning_tree_edges

def visualize_graph(graph, min_spanning_tree_edges):
    pos = nx.spring_layout(graph)  # Set the layout for the nodes

    # Draw the graph with edges in grey
    nx.draw(graph, pos, with_labels=True, font_weight='bold', edge_color='grey', node_color='lightblue')

    # Draw the minimum spanning tree edges in red
    nx.draw_networkx_edges(graph, pos, edgelist=min_spanning_tree_edges, edge_color='red', width=2)

    plt.show()

# Create a small graph for testing
random.seed(42)
G = nx.Graph()
nodes = range(1, 7)
edges = [(1, 2, random.randint(1, 10)),
         (1, 3, random.randint(1, 10)),
         (2, 3, random.randint(1, 10)),
         (2, 4, random.randint(1, 10)),
         (3, 5, random.randint(1, 10)),
         (4, 5, random.randint(1, 10)),
         (4, 6, random.randint(1, 10)),
         (5, 6, random.randint(1, 10))]
G.add_weighted_edges_from(edges)

# Apply Boruvka's algorithm
min_spanning_tree_edges = boruvka(G)

# Visualize the graph with the minimum spanning tree
visualize_graph(G, min_spanning_tree_edges)