# Chapter 4: Quicksort — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/19/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
Quicksort is a divide-and-conquer sorting algorithm that selects a pivot element and partitions the remaining elements into smaller and larger sub-arrays. The algorithm recursively sorts the sub-arrays and combines them with the pivot until the entire list becomes sorted.

- **Time complexity:**  
- Best Case: O(n log n)  
- Average Case: O(n log n)  
- Worst Case: O(n²)

- **When to use it:**  
Quicksort is useful for efficiently sorting large datasets. It is widely used because of its strong average-case performance and relatively low memory usage compared to some other sorting algorithms.

---

## Quicksort Concepts

### Divide and Conquer

Quicksort uses a divide-and-conquer strategy by repeatedly splitting the array into smaller sub-arrays around a pivot element. Each recursive call reduces the problem size until the arrays become small enough to sort directly.

---

### The Three Steps

1. **Choose Pivot:**  
The first element of the array is selected as the pivot.

2. **Partition:**  
The remaining elements are divided into two groups:
- elements less than or equal to the pivot
- elements greater than the pivot

3. **Recurse and Combine:**  
Quicksort recursively sorts both partitions and combines them with the pivot placed between the sorted sub-arrays.

---

### Trace Example

#### quicksort([3, 5, 2, 1, 4])

```text
Pivot = 3
less = [2, 1]
greater = [5, 4]

quicksort([2, 1])
Pivot = 2
less = [1]
greater = []
Combine = [1, 2]

quicksort([5, 4])
Pivot = 5
less = [4]
greater = []
Combine = [4, 5]

Final combine = [1, 2, 3, 4, 5]
```

---

### Program Output

```text
[2, 3, 5, 10]
[10, 15, 33]
[1, 2, 3, 4, 5]
[1]
[]
[1, 2, 3, 4, 5, 6, 7, 8]
```

---

### Complexity Analysis

| Case | Time Complexity | Explanation |
|------|-----------------|-------------|
| Best | O(n log n) | The pivot divides the array into balanced halves. |
| Average | O(n log n) | Most random datasets produce reasonably balanced partitions. |
| Worst | O(n²) | Occurs when the pivot repeatedly creates highly unbalanced partitions, such as with sorted arrays. |

---

## Reflection Questions

1. **What happens if the array is already sorted and you always pick the first element as pivot?**

Choosing the first element as the pivot for an already sorted array creates extremely unbalanced partitions. This causes quicksort to degrade into its worst-case performance of O(n²) because each recursive call only reduces the problem size by one element.

2. **How could you improve pivot selection to avoid worst-case performance?**

Using randomized pivot selection or the median-of-three method helps create more balanced partitions. Balanced partitions reduce recursion depth and improve the algorithm’s efficiency.

3. **How does quicksort compare to other sorting algorithms such as bubble sort or merge sort?**

Quicksort is significantly faster than bubble sort because it reduces the number of unnecessary comparisons and swaps. Compared to merge sort, quicksort generally uses less memory and performs very efficiently in practice, although merge sort guarantees O(n log n) performance in all cases.

---

## Challenges Encountered

One challenge during this lab was understanding how recursive partitioning divided the array into smaller sub-arrays. Tracing the pivot selection and printing intermediate partitions helped visualize how the algorithm gradually sorted the entire dataset through recursive calls.
