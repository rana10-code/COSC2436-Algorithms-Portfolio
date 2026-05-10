# Chapter 8: Balanced Trees (AVL) — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/02/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
An AVL tree is a self-balancing Binary Search Tree that automatically maintains balance after insertions and deletions. The tree calculates a balance factor for each node and performs rotations whenever the balance factor exceeds the allowed range of -1 to 1.

- **Time complexity:**  
- Search: O(log n)  
- Insert: O(log n)  
- Delete: O(log n)

- **When to use it:**  
AVL trees are useful when fast searching, insertion, and deletion operations are required while maintaining a balanced tree structure. They are ideal for applications requiring consistently efficient lookup performance.

---

## AVL Tree Concepts

### Balance Factor

The balance factor of a node is calculated as:

```text
Height(left subtree) - Height(right subtree)
```

AVL trees maintain a balance factor between:

```text
-1 to 1
```

If a node becomes unbalanced, rotations are performed to restore balance.

---

## Rotation Cases

| Case | Imbalance Type | Fix |
|------|----------------|-----|
| LL | Left-Left | Perform a single right rotation |
| RR | Right-Right | Perform a single left rotation |
| LR | Left-Right | Perform a left rotation on the left child, then a right rotation |
| RL | Right-Left | Perform a right rotation on the right child, then a left rotation |

---

## Test Results

### Program Output

```text
All tests passed successfully.

AVL tree remained balanced after insertions.

Rotation cases tested:
- LL Rotation
- RR Rotation
- LR Rotation
- RL Rotation
```

### Performance Table

| Operation | Time Complexity | Result |
|------------|----------------|--------|
| Search | O(log n) | Efficient |
| Insert | O(log n) | Balanced tree maintained |
| Delete | O(log n) | Tree remains balanced |

---

## Reflection Questions

1. **Why is an unbalanced BST bad?**

An unbalanced Binary Search Tree can degrade into a structure similar to a linked list. This causes search, insertion, and deletion operations to slow from O(log n) to O(n), significantly reducing efficiency.

2. **How do rotations maintain the BST property?**

Rotations rearrange nodes while preserving the in-order relationship between values. This allows the tree to restore balance without violating the Binary Search Tree property.

3. **What other self-balancing trees exist besides AVL trees?**

Other self-balancing trees include Red-Black Trees, Splay Trees, and B-Trees. Each structure uses different balancing strategies to maintain efficient operations.

---

## Challenges Encountered

One challenge during this lab was understanding how AVL rotations corrected imbalance cases, especially the Left-Right (LR) and Right-Left (RL) rotations. Drawing tree diagrams and tracing insertions step-by-step helped visualize how rotations restored balance while preserving the BST structure.
