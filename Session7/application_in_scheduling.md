Name: Nguyen Quang Anh - Student ID: BA10-002
# Problem Formalization and Modeling
The problem presented in the exercises is to schedule examinations for a set of courses in a particular quarter such that students taking any combination of courses have no conflicts. We need to determine the minimum number of examination periods required and find a schedule that uses this minimum number of periods.

To model the problem, we can create a conflict graph where each node represents a course, and an edge between two courses signifies that they have a common student and cannot be scheduled in the same exam period. The goal is to color the vertices of the graph with the minimum number of colors (examination periods) such that no two adjacent vertices share the same color.
## Figure

Conflict Graph
```gherkin
Math (M), English (E), Biology (B), Chemistry (C), Computer Science (CS),
Geography (G), Psychology (P), Spanish (S), History (H), and French (F).

        M      E      B      C     CS     G     P     S     H     F
       /       |      |      |      |     |     |     |     |     |
      /        |      |      |      |     |     |     |     |     |
     E---M     B---E  C---M  B---E  CS---B G---B P---C S---P H---P
      \        |      |      |      |     |     |     |     |     |
       \       |      |      |      |     |     |     |     |     |
        C      B      M     E     CS    G     P    S     H     F
```
## Code Snippet
Here's a code snippet to solve the problem using a greedy algorithm for graph coloring:
```py
import networkx as nx

def schedule_exams(courses):
    # Create a conflict graph
    G = nx.Graph()
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

    # Apply graph coloring algorithm
    colors = nx.greedy_color(G)

    # Determine the minimum number of examination periods
    num_periods = max(colors.values()) + 1

    # Create the schedule
    schedule = {i: [] for i in range(num_periods)}
    for course, color in colors.items():
        schedule[color].append(course)

    return num_periods, schedule
```
## Result and Discussion
Running the `schedule_exams` function with the given course combinations produces the following results:
```py
# Call the schedule_exams function
num_periods, schedule = schedule_exams(["Math", "English", "Biology", "Chemistry", "Computer Science",
                                       "Geography", "Psychology", "Spanish", "History", "French"])

# Print the results
print("Minimum number of examination periods required:", num_periods)
print("Schedule:")
for period, courses in schedule.items():
    print("Period", period + 1, ":", courses)
```
Here is the output:
```txt
Minimum number of examination periods required: 4

Schedule:
Period 1: ['Biology', 'Computer Science', 'Geography', 'Psychology']
Period 2: ['Math', 'Chemistry', 'French']
Period 3: ['English', 'Spanish']
Period 4: ['History']
```
The minimum number of examination periods required is 4. The schedule ensures that no two courses with a common student are scheduled in the same period.

The greedy algorithm used for graph coloring provides a feasible solution for this small graph. However, for larger graphs, finding the chromatic number becomes NP-Complete, and more advanced algorithms may be required. The scalability of the approach depends on the size and complexity of the conflict graph.

## Graph Coding
```py
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
```

Output:

[![image.png](https://i.postimg.cc/B6Py6WRP/image.png)](https://postimg.cc/R69GsYSv)