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

# Call the schedule_exams function
num_periods, schedule = schedule_exams(["Math", "English", "Biology", "Chemistry", "Computer Science",
                                       "Geography", "Psychology", "Spanish", "History", "French"])

# Print the results
print("Minimum number of examination periods required:", num_periods)
print("Schedule:")
for period, courses in schedule.items():
    print("Period", period + 1, ":", courses)