# Chapter 1 Lab Report: Binary Search

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 01/29/2026
- **Course:** COSC 2436

## Algorithm Summary


### Linear Search

#### Description
- Linear search iterates over each element in the array, comparing it with the target item.
It stops when the target is found or the end of the array is reached.

#### Time Complexity: (O(n))

#### When to Use
- Suitable for small datasets or unsorted data when simplicity is a priority.


### Binary Search

#### Description
- Binary search requires a sorted array. It repeatedly divides the search interval in half, checking the middle element, and determines if the target could be in the left or right sub-array.

#### Time Complexity: (O(\log n))

#### When to Use
- Ideal for searching in large, sorted datasets when fast performance is required.

## Test Results

Binary Search vs Linear Search Time Comparison
================================================
Searching in a sorted list of 128 numbers

Searching for: 1
Linear search time: 0.00000191 seconds
Binary search time: 0.00000286 seconds
Linear search result: 0
Binary search result: 0
Binary search is 0.67x faster

Searching for: 64
Linear search time: 0.00000310 seconds
Binary search time: 0.00000072 seconds
Linear search result: 63
Binary search result: 63
Binary search is 4.33x faster

Searching for: 128
Linear search time: 0.00000358 seconds
Binary search time: 0.00000167 seconds
Linear search result: 127
Binary search result: 127
Binary search is 2.14x faster

Searching for: 50
Linear search time: 0.00000191 seconds
Binary search time: 0.00000191 seconds
Linear search result: 49
Binary search result: 49
Binary search is 1.00x faster

Searching for: 100
Linear search time: 0.00000286 seconds
Binary search time: 0.00000143 seconds
Linear search result: 99
Binary search result: 99
Binary search is 2.00x faster

Searching for: 25
Linear search time: 0.00000167 seconds
Binary search time: 0.00000167 seconds
Linear search result: 24
Binary search result: 24
Binary search is 1.00x faster

Searching for: 75
Linear search time: 0.00000286 seconds
Binary search time: 0.00000167 seconds
Linear search result: 74
Binary search result: 74
Binary search is 1.71x faster

Searching for: 10
Linear search time: 0.00000048 seconds
Binary search time: 0.00000072 seconds
Linear search result: 9
Binary search result: 9
Binary search is 0.67x faster

Searching for: 90
Linear search time: 0.00000191 seconds
Binary search time: 0.00000048 seconds
Linear search result: 89
Binary search result: 89
Binary search is 4.00x faster

Searching for: 200
Linear search time: 0.00000286 seconds
Binary search time: 0.00000095 seconds
Linear search result: None
Binary search result: None
Binary search is 3.00x faster

Lab Challenge Answer:
Maximum steps for binary search in 128 items:
log2(128) = 7 steps maximum

### Search / Sort Labs
| Input Size | Comparisons (Linear/Binary) | Time (s) (Linear/Binary)     |
|------------|-----------------------------|------------------------------|
| 128        | 63 / 7                      | 0.00000191 / 0.00000286      |
| 128        | 63 / 7                      | 0.00000310 / 0.00000072      |
| 128        | 127 / 7                     | 0.00000358 / 0.00000167      |
| 128        | 49 / 6                      | 0.00000191 / 0.00000191      |
| 128        | 99 / 7                      | 0.00000286 / 0.00000143      |
| 128        | 24 / 6                      | 0.00000167 / 0.00000167      |
| 128        | 74 / 7                      | 0.00000286 / 0.00000167      |
| 128        | 9 / 4                       | 0.00000048 / 0.00000072      |
| 128        | 89 / 7                      | 0.00000191 / 0.00000048      |
| 128        | N/A                         | 0.00000286 / 0.00000095      |
