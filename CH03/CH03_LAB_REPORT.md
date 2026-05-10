# Lab 3: Recursion

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/12/2026

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:** This is the condition that stops the recursion. It identifies when the function should return a value without making further recursive calls.
2. **Recursive Case:** This part of the function solves a smaller part of the problem and calls itself with this smaller input until it reaches the base case.

### The Call Stack
The call stack is how Python keeps track of function calls. Each time a function is called, it is added to the call stack. When a function returns, it is removed from the call stack. For example, calling `fact(4)` would build the stack with `fact(4)`, `fact(3)`, `fact(2)`, and `fact(1)`, returning in reverse order.

## Function Analysis

| Function         | Base Case                | Recursive Case             | Time Complexity |
|------------------|--------------------------|----------------------------|-----------------|
| countdown        | i <= 0                   | countdown(i-1)             | O(n)            |
| fact             | x <= 1                   | x * fact(x-1)              | O(n)            |
| recursive_sum    | empty list               | arr[0] + recursive_sum(arr[1:]) | O(n)        |
| recursive_count  | empty list               | 1 + recursive_count(arr[1:])     | O(n)        |
| recursive_max    | single item list         | max(arr[0], recursive_max(arr[1:])) | O(n)        |

## Reflection Questions

1. **What happens if you forget the base case?**
   - Omitting the base case leads to infinite recursion, which results in a stack overflow error because the function calls itself indefinitely.

2. **Why is the naive Fibonacci implementation inefficient?**
   - It recalculates the same values multiple times, leading to exponential time complexity. More efficient versions use memoization to store previously calculated results.

3. **Draw the call stack for `fact(4)`.**

fact(4)
└─ fact(3)
   └─ fact(2)
      └─ fact(1)
         └─ returns 1
      └─ returns 2 * 1 = 2
   └─ returns 3 * 2 = 6
└─ returns 4 * 6 = 24
