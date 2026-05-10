# Chapter 3: Recursion — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/12/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
Recursion is a programming technique where a function calls itself to solve smaller versions of the same problem. Every recursive function contains a base case that stops the recursion and a recursive case that reduces the problem size until the base case is reached.

- **Time complexity:**  
Most recursive functions in this lab operate with O(n) time complexity because they process one element or recursive step at a time.

- **When to use it:**  
Recursion is useful for problems that can naturally be divided into smaller subproblems, such as factorial calculations, tree traversal, divide-and-conquer algorithms, and searching nested structures.

---

## Recursion Concepts

### Two Parts of Every Recursive Function

1. **Base Case:**  
The base case is the condition that stops the recursion. It identifies when the function should return a value without making additional recursive calls.

2. **Recursive Case:**  
The recursive case reduces the problem into a smaller version and calls the function again until the base case is reached.

---

## The Call Stack

The call stack is how Python keeps track of active function calls. Every time a recursive function is called, a new frame is added to the stack. When a function completes, it is removed from the stack in reverse order.

For example, calling `fact(4)` creates the following call stack:

```text
fact(4)
└─ fact(3)
   └─ fact(2)
      └─ fact(1)
         └─ returns 1
      └─ returns 2 * 1 = 2
   └─ returns 3 * 2 = 6
└─ returns 4 * 6 = 24
```

---

## Function Analysis

| Function | Base Case | Recursive Case | Time Complexity |
|----------|------------|----------------|-----------------|
| countdown | i <= 0 | countdown(i - 1) | O(n) |
| fact | x <= 1 | x * fact(x - 1) | O(n) |
| recursive_sum | empty list | arr[0] + recursive_sum(arr[1:]) | O(n) |
| recursive_count | empty list | 1 + recursive_count(arr[1:]) | O(n) |
| recursive_max | single item list | max(arr[0], recursive_max(arr[1:])) | O(n) |

---

## Reflection Questions

1. **What happens if you forget the base case?**

Without a base case, recursion continues indefinitely because the function keeps calling itself repeatedly. This eventually causes a stack overflow or recursion depth error because memory usage continues increasing until the program crashes.

2. **Why is the naive Fibonacci implementation inefficient?**

The naive recursive Fibonacci implementation repeatedly recalculates the same values many times. This creates exponential time complexity and causes the program to become extremely slow for larger inputs. Memoization improves efficiency by storing previously computed results.

3. **Why is recursion considered useful despite its overhead?**

Recursion simplifies complex problems by breaking them into smaller subproblems that follow the same structure. Although recursion can use more memory because of the call stack, it often produces cleaner and easier-to-understand solutions for problems such as tree traversal and divide-and-conquer algorithms.

---

## Challenges Encountered

One challenge during this lab was understanding how recursive calls build and return through the call stack. Tracing smaller examples step-by-step and visualizing the stack frames helped clarify how recursive functions eventually return their final results.
