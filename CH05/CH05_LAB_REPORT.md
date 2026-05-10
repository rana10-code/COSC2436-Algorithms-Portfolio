# Chapter 5: Hash Tables — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/26/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
A hash table stores data using key-value pairs. A hash function converts each key into an index where the value will be stored in an array. When two keys generate the same index, a collision occurs. In this lab, collisions were handled using linear probing, which searches sequentially for the next available slot.

- **Time complexity:**  
- Average Case: O(1)  
- Worst Case: O(n)

- **When to use it:**  
Hash tables are useful when fast searching, insertion, and deletion are required. They are commonly used in databases, dictionaries, caches, and applications that require efficient data lookup.

---

## Key Concepts

### Hash Table

A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index within an array where each value is stored.

### Linear Probing

Linear probing is a collision resolution technique where the algorithm checks the next available position in the table whenever a collision occurs.

---

## Test Results

### Program Output

```text
100
200
300
None
```

### Performance Table

| Operation | Average Time Complexity | Worst Case |
|------------|-------------------------|-------------|
| Insert     | O(1)                    | O(n)        |
| Search     | O(1)                    | O(n)        |
| Delete     | O(1)                    | O(n)        |

---

## Reflection Questions

1. **What are the advantages of using a hash table?**

Hash tables provide very fast average performance for searching, inserting, and deleting data. Most operations can be completed in constant time, O(1), making hash tables highly efficient for large datasets.

Another advantage is that values can be accessed directly using keys, which makes hash tables useful for applications such as dictionaries, caches, and databases.

2. **How does the hash function affect the performance of a hash table?**

The hash function determines how evenly keys are distributed throughout the table. A good hash function minimizes collisions and improves performance by spreading values uniformly across available indexes.

Poor hash functions generate excessive collisions, causing more probing and reducing efficiency.

3. **What are other collision resolution techniques besides linear probing?**

Other collision resolution methods include quadratic probing and separate chaining. Quadratic probing searches using increasing intervals rather than sequential positions, reducing clustering problems.

Separate chaining stores multiple elements at the same index using linked lists or other structures, allowing collisions to be handled without searching for another empty slot.

---

## What I Learned

This lab helped me understand how hash tables efficiently store and retrieve data using key-value pairs. I learned that the hash function plays an important role in determining where data is stored and how collisions occur.

I also learned how linear probing resolves collisions by searching for the next available position in the table instead of overwriting existing data. This demonstrated the importance of effective collision handling for maintaining good performance.

---

## Challenges Encountered

One challenge during this lab was understanding how collisions affected insertion and search operations. Initially, some keys were overwriting existing values because the probing logic was incorrect.

Tracing indexes step-by-step and printing the table contents after each insertion helped verify that linear probing correctly searched for the next available slot instead of replacing existing entries.
