# Lab 2: Selection Sort

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/05/2026

## Algorithm Analysis

### Selection Sort
- **Time Complexity:** O(n²)
- **How it works:** 
  1. Iterate through the list.
  2. For each position, find the smallest (or largest if reversing) element in the unsorted portion.
  3. Swap it with the first unsorted element.
  4. Repeat until the list is sorted.

## Array vs Linked List Analysis

| Operation | Array  | Linked List | Why?                                      |
|-----------|--------|-------------|-------------------------------------------|
| Read      | O(1)   | O(n)        | Direct index access for arrays.           |
| Insert    | O(n)   | O(1)*       | Linked lists don't require shifting data. |
| Delete    | O(n)   | O(1)*       | Linked lists manage pointers rather than data shift. |

\* For linked lists, O(1) insertions/deletions occur at the head.

## Reflection Questions

1. **Why is selection sort O(n²)?**
   - It involves two nested loops: one to iterate over the array and another to find the smallest element in the remaining unsorted portion, leading to O(n²) complexity.

2. **When would you choose a linked list over an array?**
   - When frequent insertions and deletions at the beginning or middle of the list are required, as linked lists provide efficient O(1) operations for these cases compared to O(n) for arrays.
