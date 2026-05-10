# Chapter 1: Binary Search vs Linear Search — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 01/29/2026
- **Course:** COSC 2436

---

## Algorithm Summary

### Linear Search

#### How It Works
Linear search iterates through each element in an array one at a time until the target value is found or the end of the array is reached.

#### Time Complexity
- **Best Case:** O(1)
- **Worst Case:** O(n)

#### When to Use It
Linear search is useful for small datasets or unsorted data where simplicity is more important than performance.

---

### Binary Search

#### How It Works
Binary search works on a sorted array by repeatedly dividing the search interval in half. The algorithm compares the target value with the middle element and continues searching in the appropriate half of the array.

#### Time Complexity
- **Best Case:** O(1)
- **Worst Case:** O(log n)

#### When to Use It
Binary search is ideal for large sorted datasets because it significantly reduces the number of comparisons required.

---

## Test Results

### Program Output

```text
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
```

### Search Results Table

| Target Value | Linear Search Result | Binary Search Result | Linear Search Time (s) | Binary Search Time (s) |
|--------------|---------------------|----------------------|------------------------|-------------------------|
| 1            | 0                   | 0                    | 0.00000191             | 0.00000286              |
| 64           | 63                  | 63                   | 0.00000310             | 0.00000072              |
| 128          | 127                 | 127                  | 0.00000358             | 0.00000167              |
| 50           | 49                  | 49                   | 0.00000191             | 0.00000191              |
| 100          | 99                  | 99                   | 0.00000286             | 0.00000143              |
| 25           | 24                  | 24                   | 0.00000167             | 0.00000167              |
| 75           | 74                  | 74                   | 0.00000286             | 0.00000167              |
| 10           | 9                   | 9                    | 0.00000048             | 0.00000072              |
| 90           | 89                  | 89                   | 0.00000191             | 0.00000048              |
| 200          | None                | None                 | 0.00000286             | 0.00000095              |

### Lab Challenge Answer

For a dataset containing 128 items, the maximum number of steps required for binary search is:

```text
log2(128) = 7
```

Therefore, binary search takes at most **7 steps** in the worst-case scenario.

---

## Reflection Questions

### 1. Why is binary search faster than linear search?

Binary search eliminates half of the remaining search space after every comparison, which greatly reduces the number of operations required. Linear search checks each element sequentially, making it slower for large datasets.

### 2. Why must binary search use sorted data?

Binary search relies on ordered data to determine whether the target value is located in the left or right half of the array. Without sorting, the algorithm cannot correctly eliminate half of the remaining elements.

### 3. When would linear search still be useful?

Linear search is useful for small datasets or unsorted collections where simplicity is more important than performance. It is also practical when the overhead of sorting data is unnecessary.

---

## Challenges Encountered

One challenge during this lab was correctly updating the low and high indexes during binary search. Testing the algorithm with small arrays and tracing each iteration step-by-step helped verify that the search interval was shrinking correctly and producing accurate results.
