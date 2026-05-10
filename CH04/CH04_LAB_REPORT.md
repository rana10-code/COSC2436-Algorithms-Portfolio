# Lab 04: Quicksort

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/19/2026

## Quicksort Concepts

### Divide and Conquer
Quicksort employs a divide-and-conquer approach by repeatedly dividing an array into smaller sub-arrays around a pivot, sorting those, and combining results. This reduces the problem size with each recursive call.

### The Three Steps
1. **Choose pivot:** The first element of the array is chosen as the pivot.
2. **Partition:** Divide the array into two sub-arrays: one with elements less than or equal to the pivot, and one with elements greater than the pivot.
3. **Recurse and combine:** Recursively apply quicksort to the sub-arrays and concatenate the sorted sub-arrays with the pivot in between.

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
1. `Pivot = 3`, `less = [2, 1]`, `greater = [5, 4]`
   - quicksort([2, 1])
     - Pivot = 2, `less = [1]`, `greater = []`
     - Combine = [1, 2]
   - quicksort([5, 4])
     - Pivot = 5, `less = [4]`, `greater = []`
     - Combine = [4, 5]
   - Final combine = [1, 2, 3, 4, 5]

## Complexity Analysis

| Case    | Time Complexity | Why?                                    |
|---------|-----------------|-----------------------------------------|
| Best    | O(n log n)      | Occurs when the pivot divides the array into two nearly equal halves. |
| Average | O(n log n)      | Random distribution of elements gives balanced division most of the time. |
| Worst   | O(n²)           | Arises when the pivot is the smallest or largest element repeatedly, such as in a sorted array. |

## Reflection Questions

1. **What happens if the array is already sorted and you always pick the first element as pivot?**
   - This leads to the worst-case time complexity (O(n²)) because the pivot is not dividing the array effectively.

2. **How could you improve pivot selection to avoid worst-case performance?**
   - Randomizing the pivot choice or using the median of the first, middle, and last elements can help optimize performance.

3. **How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?**
   - Quicksort is generally faster on average and uses less memory than merge sort, but it is less stable. It outperforms bubble sort due to better efficiency.

4. **Why do we use `array[1:]` instead of `array` when building the less and greater lists?**
   - We use `array[1:]` to exclude the pivot from the sub-arrays, preventing it from being included in recursive calls.

## Test Output

[2, 3, 5, 10]
[10, 15, 33]
[1, 2, 3, 4, 5]
[1]
[]
[1, 2, 3, 4, 5, 6, 7, 8]
