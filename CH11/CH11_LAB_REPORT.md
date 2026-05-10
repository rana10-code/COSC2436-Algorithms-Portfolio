# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/23/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** The dynamic programming approach to the knapsack problem constructs a 2D grid to represent the optimal set of items for given weight capacities. Decisions are made to include or exclude items to maximize the total value without exceeding the weight limit.
- **Time complexity:** O(n * W), where n is the number of items and W is the knapsack capacity.
- **When to use it:** Suitable for optimization problems with overlapping subproblems and a need for optimal sequential decision-making.

## Test Results

| Item List                                           | Capacity | Result                  | Notes                                      |
|-----------------------------------------------------|----------|-------------------------|--------------------------------------------|
| ("GUITAR", "STEREO", "LAPTOP", "iPHONE", "BOOK")    | 6        | Max Value = $35,500     | Selection: GUITAR, LAPTOP, iPHONE, GOLD BAR |

## Reflection Questions

1. **What did you learn about dynamic programming through this lab?**
   Dynamic programming effectively solves problems by leveraging previously computed solutions to overlap subproblems, leading to efficient and optimal decision-making.

2. **Why is it important to copy lists rather than using direct assignments in the grid?**
   Copying lists ensures each grid cell is independent, preventing changes in one solution from affecting others and maintaining solution integrity.

3. **How does this approach differ from a greedy algorithm for the same problem?**
   Dynamic programming evaluates all combinations to ensure a global optimum, whereas greedy algorithms make local choices that may not result in the best overall solution.

## Challenges Encountered
Managing grid updates without reference overlap was challenging. Using slicing (`[:]`) to create copies of lists resolved this issue and maintained independent solutions. Formatting the grid output required careful handling to ensure alignment and display were consistent.
