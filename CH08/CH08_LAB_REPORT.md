# Chapter 08: Balanced Trees (AVL) — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/02/2026

## Algorithm Analysis

### AVL Trees
- **Balance Factor Range:** -1 to 1
- **Why rebalance?** Rebalancing keeps the tree height-balanced, ensuring that operations such as insertion, deletion, and lookups remain efficient with a time complexity of O(log n). Without rebalancing, the tree could become skewed and degrade operation efficiency.
- **Time Complexity (all operations):** O(log n). The tree maintains a balanced height through rotations, so operations are logistically efficient.

### Rotation Cases
| Case | Imbalance | Fix |
|------|-----------|-----|
| LL   | Left-Left | Perform a single right rotation |
| RR   | Right-Right | Perform a single left rotation |
| LR   | Left-Right | Perform a left rotation on the left child, then a right rotation on the node |
| RL   | Right-Left | Perform a right rotation on the right child, then a left rotation on the node |

## Test Results
- All tests passed successfully, confirming that the AVL tree maintains balance after insertions.
- Tested various sequences of insertions including cases that trigger each type of rotation (LL, RR, LR, RL).

## Reflection Questions

1. **Why is an unbalanced BST bad?**
   - An unbalanced BST can lead to inefficient operations, degrading to O(n) time complexity as the tree becomes similar to a linked list, negating the benefits of a binary search tree.

2. **How do rotations maintain the BST property?**
   - Rotations adjust the subtree’s structure to maintain balance while preserving the in-order sequence of nodes, ensuring the integrity of the binary search property.

3. **What other self-balancing trees exist?**
   - Other self-balancing trees include Red-Black Trees, Splay Trees, and B-Trees, each using different strategies for maintaining balance.

## Challenge Encountered
- I initially struggled with understanding rotation mechanics, especially the left-right and right-left cases. I solved this by drawing out tree diagrams to visualize the process. Additionally, implementing test cases helped me solidify the concepts.
