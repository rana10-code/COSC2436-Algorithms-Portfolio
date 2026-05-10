# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/23/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
This lab used dynamic programming to solve the knapsack optimization problem. The algorithm builds a grid where each cell stores the best possible solution for a given item set and weight capacity. By reusing solutions to smaller subproblems, the algorithm efficiently computes the optimal combination of items.

- **Time complexity:**  
O(n × W), where:
- n = number of items
- W = knapsack capacity

- **When to use it:**  
Dynamic programming is useful for optimization problems involving overlapping subproblems and optimal substructure, such as the knapsack problem, shortest paths, sequence alignment, and scheduling problems.

---

## Test Results

### Program Output

```text
Items:
GUITAR
STEREO
LAPTOP
iPHONE
BOOK
GOLD BAR

Knapsack Capacity: 6

Optimal Selection:
GUITAR
LAPTOP
iPHONE
GOLD BAR

Maximum Value = $35,500
```

### Performance Table

| Item List | Capacity | Result | Notes |
|------------|----------|--------|-------|
| GUITAR, STEREO, LAPTOP, iPHONE, BOOK, GOLD BAR | 6 | Max Value = $35,500 | Optimal combination selected successfully |

---

## Reflection Questions

1. **What did you learn about dynamic programming through this lab?**

This lab demonstrated how dynamic programming efficiently solves optimization problems by storing solutions to smaller subproblems and reusing them later. Instead of recalculating values repeatedly, the algorithm builds solutions incrementally using a structured grid.

2. **Why is it important to copy lists rather than using direct assignments in the grid?**

Copying lists prevents multiple grid cells from referencing the same object in memory. Without copying, modifying one solution could unintentionally alter other stored solutions, producing incorrect results.

3. **How does this approach differ from a greedy algorithm for the same problem?**

Dynamic programming evaluates many possible combinations to guarantee the optimal solution. Greedy algorithms make locally optimal decisions step-by-step, which may not always produce the best overall result.

---

## Challenges Encountered

One challenge during this lab was managing grid updates without accidentally sharing references between cells. Using slicing (`[:]`) to create copies of lists ensured that each solution remained independent.

Another challenge involved formatting the dynamic programming table clearly so that intermediate solutions could be interpreted and debugged correctly.
