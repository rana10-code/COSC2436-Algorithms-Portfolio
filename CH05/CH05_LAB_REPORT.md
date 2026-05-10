# Lab 05: 2436 Hash Table Lab 05

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/26/2026

## Key Concepts
- **Hash Table:** A data structure that stores key-value pairs. It uses a hash function to compute an index into an array, where each key-value pair is stored.
- **Linear Probing:** A collision resolution technique where you move sequentially through the array to find an empty slot when a collision occurs.

## What I Learned
This lab helped me understand how hash tables store and retrieve data efficiently using key-value pairs. I learned that the hash function plays a major role in determining where data is stored in memory and how collisions occur.

I also learned how linear probing works as a collision resolution technique. Instead of replacing existing data during a collision, the algorithm checks the next available slot in the table until an empty location is found. This demonstrated how important collision handling is for maintaining good performance.


## Challenges
One of the most difficult parts of implementing the hash table was understanding how collisions affected insertion and search operations. Initially, some keys were overwriting existing values because the probing logic was incorrect.

I resolved this issue by tracing the indexes step-by-step and printing the table contents after each insertion. This helped verify that linear probing correctly searched for the next available slot instead of replacing existing entries.



## Reflection Questions
1. **What are the advantages of using a hash table?**  
   Discuss advantages like fast average time complexity for search, insert, and delete operations.

2. **How does the hash function affect the performance of a hash table?**  
   Explain how a good hash function distributes keys uniformly, reducing collisions and performance degradation.

3. **What are other collision resolution techniques besides linear probing?**  
   Mention alternatives like quadratic probing and separate chaining.

## Output

### 100
### 200
### 300
### None
