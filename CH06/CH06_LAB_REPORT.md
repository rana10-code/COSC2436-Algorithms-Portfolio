# Lab 06: Breadth-First Search

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 03/05/2026

## Key Concepts
- **Graph Data Structures:** Graphs consist of nodes (vertices) connected by edges. In this lab, we represented the Texas road network as an undirected graph using an adjacency list.
- **Breadth-First Search (BFS):** BFS explores nodes level by level from the starting node, using a queue to track the order of exploration. It's ideal for finding the shortest path by the number of edges in unweighted graphs.
- **Shortest Path:** BFS finds the shortest path in terms of edges. It visits each node's neighbors before moving to the next level, ensuring the shortest path for unweighted graphs.

## What I Learned
I learned to implement the BFS algorithm in Python, particularly in using a queue for level-order traversal. I also deepened my understanding of graph representations using adjacency lists, which offer space efficiency for sparse graphs.

## Challenges
The most difficult part was debugging the BFS implementation to correctly track visited nodes and ensure all paths were explored. I overcame this by adding print statements to trace the queue's state and visiting order, which helped identify when nodes were incorrectly revisited.

## Reflection Questions
1. **Why does BFS use a queue instead of a stack?**
   BFS uses a queue to process nodes in the order they are discovered, ensuring that nodes are explored layer by layer. This first-in, first-out (FIFO) approach is crucial to exploring the shallowest nodes first.
   
2. **What's the difference between BFS shortest path and actual shortest distance?**
   BFS finds the shortest path based on the number of edges, not actual physical distances. For weighted graphs where distance matters, algorithms like Dijkstra's or A* are better suited.

3. **When would you use BFS vs DFS?**
   Use BFS when you need the shortest path in an unweighted graph, or when exploring nodes closest to a source first. DFS is better for exploring all paths in a graph (e.g., finding connectivity).

## Output

============================================================
PART 1: TEXAS ROAD NETWORK GRAPH
============================================================

Created graph with 18 cities

Graph Adjacency List:
----------------------------------------
Arlington: ['Dallas', 'Fort Worth']
Austin: ['Dallas', 'San Antonio', 'Killeen']
Brownsville: ['Corpus Christi', 'McAllen']
Corpus Christi: ['Houston', 'San Antonio', 'Brownsville']
Dallas: ['Houston', 'Austin', 'Fort Worth', 'Arlington', 'Plano', 'Irving', 'Garland']
El Paso: ['San Antonio', 'Lubbock']
Fort Worth: ['Dallas', 'Lubbock', 'Arlington']
Frisco: ['Plano']
Garland: ['Dallas']
Houston: ['Dallas', 'San Antonio', 'Corpus Christi']
Irving: ['Dallas']
Killeen: ['Austin']
Laredo: ['San Antonio', 'McAllen']
Lubbock: ['Fort Worth', 'El Paso']
McAllen: ['Brownsville', 'Laredo']
McKinney: ['Plano']
Plano: ['Dallas', 'Frisco', 'McKinney']
San Antonio: ['Austin', 'Laredo', 'Houston', 'El Paso', 'Corpus Christi']

============================================================
PART 2: SHORTEST PATH (BFS)
============================================================

Route: Houston → San Antonio → El Paso

----------------------------------------

Route: Houston → Dallas → Plano → McKinney

============================================================
PART 3: DISTANCES FROM HOUSTON
============================================================

Cities by distance (edges) from Houston:
  0 edge(s): Houston
  1 edge(s): Corpus Christi, Dallas, San Antonio
  2 edge(s): Arlington, Austin, Brownsville, El Paso, Fort Worth, Garland, Irving, Laredo, Plano
  3 edge(s): Frisco, Killeen, Lubbock, McAllen, McKinney

============================================================
PART 4: BFS KEY CONCEPTS
============================================================

    Why BFS finds shortest path:
    1. Explores ALL nodes at distance 1 first
    2. Then ALL nodes at distance 2
    3. And so on...
    
    First time we reach destination = shortest path!
    
    BFS uses a QUEUE (FIFO):
    - First In, First Out
    - Process nodes in order they were discovered
    
    Time Complexity: O(V + E)
    - Visit each vertex once: O(V)
    - Check each edge once: O(E)
    
    Note: BFS finds shortest path by NUMBER OF EDGES.
    For weighted graphs (actual distances), use Dijkstra's (Lab 9)!
