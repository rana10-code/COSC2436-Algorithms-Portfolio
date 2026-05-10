# Chapter 9: Dijkstra's Algorithm — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/09/2026
- **Course:** COSC 2436

---

## Algorithm Analysis
- **How it works:**  
Dijkstra’s algorithm finds the shortest path between nodes in a weighted graph by repeatedly selecting the unvisited node with the smallest tentative distance. The algorithm updates the distances of neighboring nodes whenever a shorter path is discovered.

- **Time complexity:**  
- O(V²) using a simple array scan  
- O((V + E) log V) using a priority queue or min-heap

- **When to use it:**  
Dijkstra’s algorithm is useful for finding shortest paths in weighted graphs with non-negative edge weights. Common applications include GPS navigation, network routing, transportation systems, and mapping software.

---

## Test Results

### Program Output

```text
=== Dijkstra's Shortest Path ===

Enter node names one per line.

Node: book
Added: book

Node: lp
Added: lp

Node: poster
Added: poster

Node: drum
Added: drum

Node: done

book <--> lp (weight or Enter to skip): 5
Added: book <--5--> lp

book <--> poster (weight or Enter to skip): 0
Added: book <--0--> poster

book <--> drum (weight or Enter to skip):
No edge added

book <--> lp (weight or Enter to skip): -3
Invalid weight (must be non-negative)

book <--> drum (weight or Enter to skip): not a number
Skipped

Shortest path found successfully.
```

---

### Input Validation Table

| Input | Result | Notes |
|-------|--------|-------|
| book <--> lp: 5 | Added edge | Valid non-negative weight |
| book <--> poster: 0 | Added edge | Zero-weight edge accepted |
| book <--> drum: (Enter to skip) | No edge added | Empty input correctly skipped |
| book <--> lp: -3 | Invalid weight | Negative weights rejected |
| book <--> drum: not a number | Skipped | Non-numeric input rejected |

---

## Reflection Questions

1. **Why initialize all node costs to infinity except for the start node?**

Initializing all node costs to infinity establishes a starting comparison value larger than any possible path cost. This allows the algorithm to correctly update node distances whenever a shorter path is discovered during traversal.

2. **Why store edges in both directions for undirected graphs?**

Undirected graphs allow movement between connected nodes in both directions. Storing edges in both directions ensures that Dijkstra’s algorithm can correctly traverse the graph regardless of the starting point.

3. **What problems occur with negative edge weights in Dijkstra’s algorithm?**

Dijkstra’s algorithm assumes that path costs only increase as traversal continues. Negative edge weights can violate this assumption and cause incorrect shortest-path calculations. Algorithms such as Bellman-Ford are better suited for graphs containing negative weights.

---

## Challenges Encountered

One challenge during this lab was correctly implementing graph construction and validating user input for edge weights. Another difficulty involved visually representing the graph and tracing shortest-path calculations step-by-step. Systematic testing with different node configurations and debugging edge cases helped verify the correctness of the implementation.
