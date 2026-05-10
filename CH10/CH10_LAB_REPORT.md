# Chapter 10: Greedy Algorithms (Truck Packing) — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/16/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
This greedy algorithm solves a truck packing optimization problem by selecting boxes based on volume. The algorithm sorts boxes in descending order by size and packs the largest boxes first until the truck reaches its maximum capacity.

- **Time complexity:**  
O(n log n) due to sorting the boxes before packing.

- **When to use it:**  
Greedy algorithms are useful when fast approximate solutions are acceptable. They work well for optimization problems where making locally optimal decisions can produce a reasonably efficient overall solution.

---

## Algorithm Understanding

### What type of problem is this algorithm solving?

This algorithm solves a packing optimization problem where boxes must be selected and packed efficiently within a truck’s capacity constraints.

### Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?

No, the greedy algorithm is not guaranteed to produce the optimal solution because it makes locally optimal choices without evaluating all possible combinations of boxes.

### What is the greedy choice made in this algorithm?

The greedy choice is to prioritize larger boxes by sorting them in descending order of volume and packing them first.

---

## Implementation Questions

### Why do we sort the boxes in descending order of volume before packing?

Sorting by descending volume ensures that larger boxes are packed first, maximizing space utilization early in the packing process.

### What would happen if we sorted the boxes in ascending order instead?

Sorting in ascending order could leave awkward unused space that prevents larger boxes from fitting later, reducing packing efficiency.

### Why do we keep track of `used_volume`?

Tracking `used_volume` ensures that the total packed volume never exceeds the truck’s capacity.

---

## Extension: Dimension Constraints

### Why is checking only volume not sufficient for real-world packing?

Volume alone does not account for the physical dimensions and orientation of boxes. A box may fit by total volume but still fail to physically fit inside the truck.

### Give an example where a box fits by volume but not by dimensions.

A long box with dimensions 10x1x1 may have a small volume but still not fit inside a truck with a width smaller than 10 units.

### How would you modify the algorithm to check dimension constraints before packing a box?

The algorithm would compare each box’s length, width, and height against the truck’s dimensions before allowing it to be packed.

---

## Test Results

| Input | Result | Notes |
|-------|--------|-------|
| Truck: 5x5x5, Box: 2x2x2 | Box fits | Single box fits successfully |
| Truck: 5x5x5, Boxes: 2x2x2, 2x2x1 | Both boxes fit | Multiple boxes packed successfully |
| Truck: 5x5x5, Boxes: 10x10x10 | Box does not fit | Exceeds truck capacity |
| Truck: 5x5x5, Multiple 2x2x2 boxes | Some boxes fit | Edge case for volume utilization |
| Invalid input values | Error message displayed | Input validation handled correctly |

---

## Reflection Questions

1. **What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**

The greedy algorithm may fail when selecting large boxes first prevents better combinations of smaller boxes from fitting efficiently. In some cases, multiple small boxes may utilize the available space more effectively than one large box.

2. **How is this problem related to the Knapsack Problem?**

The truck packing problem is similar to the Knapsack Problem because both involve selecting items within a limited capacity while maximizing efficiency or value.

3. **What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**

Dynamic programming algorithms can guarantee optimal solutions because they evaluate many possible combinations systematically. However, they require significantly more computation time and memory than greedy approaches.

4. **If the truck had weight limits in addition to volume, how would the algorithm need to change?**

The algorithm would need to track both total weight and total volume simultaneously before adding boxes. Selection decisions would likely consider both dimensions rather than volume alone.

5. **Why are greedy algorithms often preferred despite not always being optimal?**

Greedy algorithms are preferred because they are simple, fast, and often produce good approximate solutions efficiently. In many real-world applications, obtaining a fast near-optimal solution is more practical than computing the perfect solution.

---

## Challenges Encountered

One challenge during this lab was determining how to prioritize boxes for efficient packing. Initially, considering only volume caused unrealistic packing scenarios where boxes technically fit by volume but not by dimensions.

To address this issue, the algorithm was adjusted to sort boxes by descending volume while also considering dimensional constraints. Testing different box combinations helped verify that the packing logic produced more realistic results.
