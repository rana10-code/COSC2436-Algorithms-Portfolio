# Chapter 7: Binary Trees and Tree Traversal — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 03/26/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
A Binary Search Tree (BST) is a hierarchical data structure where each node contains a value and references to left and right child nodes. The BST property ensures that values smaller than the current node are stored in the left subtree, while larger values are stored in the right subtree. Tree traversal algorithms systematically visit nodes in different orders to process or display the data.

- **Time complexity:**  
- Balanced BST Search: O(log n)  
- Unbalanced BST Search: O(n)

- **When to use it:**  
Binary Search Trees are useful for efficient searching, insertion, and deletion operations. Traversal algorithms are commonly used for sorting, copying trees, evaluating expressions, and managing hierarchical data.

---

## Traversal Types

| Traversal | Order | Common Use Case |
|-----------|-------|-----------------|
| Preorder | Root, Left, Right | Copying a tree |
| Inorder | Left, Root, Right | Producing sorted output |
| Postorder | Left, Right, Root | Deleting or freeing a tree |

---

## Test Results

### Program Output

```text
[1, 3, 5, 7, 8, 9, 10]
True
False
```

### Traversal Analysis

| Traversal Type | Result |
|----------------|--------|
| Inorder Traversal | Produces sorted values |
| Search Existing Value | True |
| Search Missing Value | False |

---

## Reflection Questions

1. **Why does inorder traversal give sorted output?**

Inorder traversal visits the left subtree first, followed by the current node, and then the right subtree. Because a Binary Search Tree stores smaller values on the left and larger values on the right, this traversal naturally processes the nodes in ascending order.

2. **When would a BST become unbalanced?**

A BST becomes unbalanced when values are inserted in already sorted order or nearly sorted order. This creates a tree structure that resembles a linked list, reducing search efficiency from O(log n) to O(n).

3. **What is the difference between BFS and DFS for trees?**

Breadth-First Search (BFS) explores nodes level-by-level using a queue, while Depth-First Search (DFS) explores one branch as deeply as possible before backtracking. DFS is commonly implemented recursively or with a stack.

---

## Challenges Encountered

One challenge during this lab was understanding how recursive tree traversals visited nodes in different orders. Printing intermediate traversal steps and manually drawing the tree structure helped verify that preorder, inorder, and postorder traversals were working correctly.
