# Chapter 09: Dijkstra's Shortest Path — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/09/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:**  
  Dijkstra's algorithm finds the shortest path from a starting node to all other nodes in a weighted graph by iteratively selecting the node with the lowest tentative distance and updating its neighbors' distances.
- **Time complexity:**  
  O(V^2) with a simple array scan for the minimum node, or O((V + E) log V) with a min-heap.
- **When to use it:**  
  Use Dijkstra's algorithm for finding the shortest path in graphs with non-negative weights, such as in network routing or geographical mapping.

## Test Results
The following results were obtained from running the program:

| Input          | Result                                 | Notes                                              |
|----------------|----------------------------------------|----------------------------------------------------|
| Nodes: book, lp, poster, bass, drum, piano | Shortest path: book → lp → drum → piano | Total cost: 35 |  

## Reflection Questions

1. **Why initialize all node costs to infinity except for the start node?**  
   Initializing to infinity sets a baseline for comparison that ensures any real path found will have a shorter path cost, thus allowing for updates as shorter paths are discovered.

2. **Why store edges in both directions for undirected graphs?**  
   Storing edges in both directions ensures that traversal is possible in any direction between connected nodes, which is essential for accurately finding the shortest paths.

3. **What issues arise with negative edge weights in Dijkstra's?**  
   Negative edge weights can cause Dijkstra's algorithm to produce incorrect results because it assumes that path costs never decrease. Bellman-Ford is better suited for graphs with negative weights.

## Challenges Encountered
Implementing the ASCII graphical representation and handling user input for constructing the graph were initial challenges. Ensuring that the graph was correctly represented as undirected required careful handling of how edges were stored. Testing the implementation with various inputs helped confirm its correctness, and systematic debugging resolved edge cases.
