# Chapter 6: Breadth-First Search (BFS) — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 03/05/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
Breadth-First Search (BFS) explores a graph level by level starting from a source node. The algorithm uses a queue to visit all neighboring nodes before moving deeper into the graph. BFS guarantees the shortest path in terms of the number of edges for unweighted graphs.

- **Time complexity:**  
O(V + E)

- **When to use it:**  
BFS is useful for finding shortest paths in unweighted graphs, exploring connected components, and traversing graphs level-by-level.

---

## Key Concepts

### Graph Data Structures

Graphs consist of nodes (vertices) connected by edges. In this lab, the Texas road network was represented as an undirected graph using an adjacency list.

### Breadth-First Search (BFS)

BFS explores neighboring nodes first before moving deeper into the graph. A queue is used to maintain the order of node exploration.

### Shortest Path

BFS guarantees the shortest path by number of edges because it visits all nodes at the current depth level before continuing to the next level.

---

## Test Results

### Program Output

```text
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
For weighted graphs (actual distances), use Dijkstra's algorithm.
```

---

## Reflection Questions

1. **Why does BFS use a queue instead of a stack?**

BFS uses a queue because it processes nodes in the order they are discovered. This first-in, first-out (FIFO) behavior ensures that nodes closer to the source are explored before deeper nodes, allowing BFS to correctly find the shortest path in unweighted graphs.

2. **What is the difference between BFS shortest path and actual shortest distance?**

BFS finds the shortest path based on the number of edges traveled, not actual physical distance or weighted cost. In weighted graphs, algorithms such as Dijkstra’s algorithm are required to calculate the true shortest distance.

3. **When would you use BFS instead of DFS?**

BFS is preferred when the shortest path in an unweighted graph is required or when exploring nodes level-by-level. DFS is more useful for exploring all possible paths, recursive traversal, and problems involving connectivity or backtracking.

---

## What I Learned

This lab helped me understand how BFS explores graphs using a queue-based level-order traversal approach. I also learned how adjacency lists efficiently represent sparse graphs and how BFS guarantees the shortest path in terms of edge count.

---

## Challenges Encountered

One challenge during this lab was correctly tracking visited nodes to prevent revisiting the same cities repeatedly. Adding debugging print statements to trace queue operations and visitation order helped identify logical errors and verify that BFS explored the graph correctly.
