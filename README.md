**Table of contents**

- [Session 1 - Introduction](#session-1---introduction)
	- [Graph Software](#graph-software)
- [Session 2 - ADT - Graph Traversal - Complexity](#session-2---adt---graph-traversal---complexity)
	- [Assignment: BFS using queue in Python](#assignment-bfs-using-queue-in-python)
- [Session 3 - Graph Traversal - Complexity](#session-3---graph-traversal---complexity)
- [Session 4 - Minimum Spanning Tree](#session-4---minimum-spanning-tree)
	- [Assignment: Minimum Spanning Trees](#assignment-minimum-spanning-trees)
- [Session 5 - Binary Trees - Huffman - Binary Search Trees](#session-5---binary-trees---huffman---binary-search-trees)
- [Session 6 - Maximum flows - Ford-Fulkerson -Edmonds and Karp](#session-6---maximum-flows---ford-fulkerson--edmonds-and-karp)
- [Session 7 - Graph Coloring](#session-7---graph-coloring)
- [Session 8 - Introduction to NP-complete problems](#session-8---introduction-to-np-complete-problems)
- [Session 9 - Complex Networks](#session-9---complex-networks)

Documents for students
# Session 1 - Introduction
- Slides: [Introduction to graphs](Session1/01-Graph-Intro.pdf)
- Code: [naïve Graph class using edge adjacency lists `basic_graph_adjlist.py`](Session1/lib/basic_graph_adjlist.py)
- Code: [naïve Graph class using adjacency matrix `basic_graph_matrix.py`](Session1/lib/basic_graph_matrix.py)
- Notebook: [plotting a graph with matplotlib](Session1/01-a-Loading-Plotting-naive.ipynb)
- Notebook: [Introduction to NetworkX](Session1/01-b-Introduction_to_networkx.ipynb)
- Notebook: [Plotting Karate Network using NetworkX](Session1/01-c-Plotting-Karate-NetworkX.ipynb)
## Graph Software
- [Gephi: The Open Graph Viz Platform](https://gephi.org/)
- Video tutorial: [Introduction to Network Analysis and Visualization](https://www.youtube.com/watch?v=GXtbL8avpik)
# Session 2 - ADT - Graph Traversal - Complexity
- Slides: [Abstract Data Types: Stack, Queues, and Dictionaries](Session2/02-Stacks-Queue-Maps.pdf)
- Slides: [Graph Traversal Algorithms, DFS](Session2/03-Graph-Traversal.pdf)
- Notebook: _A simple python implementation of DFS using Recursion_ [02-a-DFS-recursive.ipynb](Session2/02-a-DFS-recursive.ipynb)
- Code: _copy lib directory and its content_ [lib](Session2/lib)
- Data: _example graph:_ [`soc-karate.mtx`](Session2/data/soc-karate/soc-karate.mtx)
- Slides: [DFS Algorithm with a stack](Session2/04-DFS-Algo-With-Stack.pdf)
## Assignment: BFS using queue in Python
[Implement BFS using a queue in Python](Session2/dfs_implement.py)

Code the BFS (breadth-first-search) algorithm in Python using

- The Graph class provided by NetworkX
- The Queue class seen in class

Upload your work as a **unique file**, either a **.py** or a notebook **.ipynb**
# Session 3 - Graph Traversal - Complexity
- Slides: [Algorithmic Complexity](Session3/05-Algorithmic-Complexity.pdf)
- Slides: [Breadth-First-Search (BFS)](Session3/06-Graph-Traversal-BFS.pdf)
- Slides: [Dijkstra's Algorithm](Session3/07-Dijkstra.pdf)
# Session 4 - Minimum Spanning Tree
- Slides: [Prim's and Kruskal algorithms](Session4/08-MinimumSpanningTreePrim.pdf)
- Slides: [Minimum Spanning Tree: examples](Session4/08-MinimumSpanningTreeRuns.pdf)
## Assignment: Minimum Spanning Trees
**Implement a Minimum Spanning Tree Algorithm**

Implement one of 
- [Prim's algorithm](Session4/prim_algorithm_mst_implement.py)
- [Boruvka's algorithm](Session4/Boruvka_algorithm_mst_implement.py)
- Kruskal's algorithm

and apply it to a small graph of your choice.

You code will:
- build the graph
- compute a minimum spanning tree
- display the result: the edges belonging to the spanning tree in **red**, the other in **grey**
# Session 5 - Binary Trees - Huffman - Binary Search Trees
- Slides: [Binary Trees - Huffman - Binary Search Trees](Session5/05-BinaryTrees.pdf)
# Session 6 - Maximum flows - Ford-Fulkerson -Edmonds and Karp
- Slides: [Maximum Flows](Session6/06-Max-Flow.pdf)
# Session 7 - Graph Coloring
- Slides: [Graph Coloring](Session7/07-Graph-Coloring.pdf)
# Session 8 - Introduction to NP-complete problems
- Slides: [Intro. NP-complete](Session8/08-Intro-NP-Complete.pdf)
# Session 9 - Complex Networks
- Slides: [Complex Networks](Session9/09-Complex-Networks.pdf)