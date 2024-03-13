import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add courses as nodes
courses = ["Math", "English", "Biology", "Chemistry", "Computer Science",
           "Geography", "Psychology", "Spanish", "History", "French"]
G.add_nodes_from(courses)

# Add edges between conflicting courses
conflicts = [("Math", "English"), ("Math", "Biology"), ("Math", "Chemistry"),
             ("English", "Biology"), ("English", "Chemistry"), ("Biology", "Chemistry"),
             ("English", "Computer Science"), ("Biology", "Geography"),
             ("Computer Science", "Biology"), ("Geography", "Psychology"),
             ("Psychology", "Computer Science"), ("Psychology", "Chemistry"),
             ("Psychology", "Geography"), ("Psychology", "History"),
             ("Psychology", "Spanish"), ("History", "French")]
G.add_edges_from(conflicts)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
plt.title("Conflict Graph")
plt.show()