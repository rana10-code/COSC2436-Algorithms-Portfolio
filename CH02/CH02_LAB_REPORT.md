# Chapter 2: Selection Sort — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 02/05/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
Selection sort repeatedly searches the unsorted portion of the list to find the smallest element. After finding the minimum value, the algorithm swaps it with the first unsorted position. This process continues until the entire list is sorted.

- **Time complexity:**  
O(n²)

- **When to use it:**  
Selection sort is best suited for small datasets and educational purposes where simplicity and understanding the sorting process are more important than performance efficiency.

---

## Test Results

### Program Output

```text
Original Array:
[64, 25, 12, 22, 11]

Sorting...

Pass 1:
[11, 25, 12, 22, 64]

Pass 2:
[11, 12, 25, 22, 64]

Pass 3:
[11, 12, 22, 25, 64]

Pass 4:
[11, 12, 22, 25, 64]

Final Sorted Array:
[11, 12, 22, 25, 64]
```

### Performance Table

| Input | Result | Notes |
|-------|--------|-------|
| [64, 25, 12, 22, 11] | [11, 12, 22, 25, 64] | Array sorted successfully |
| Small dataset | Correct output | Performs adequately |
| Large dataset | Slower performance | O(n²) complexity causes inefficiency |

---

## Reflection Questions

1. **Why is selection sort considered inefficient for large datasets?**

Selection sort repeatedly scans the unsorted portion of the array to locate the minimum value, resulting in many comparisons. As the dataset grows, the number of operations increases significantly, making the algorithm inefficient compared to faster sorting methods such as quicksort or mergesort.

2. **What is the main idea behind selection sort?**

The main idea behind selection sort is to repeatedly find the smallest element from the unsorted portion of the array and move it to its correct sorted position. The sorted portion gradually grows while the unsorted portion becomes smaller after each pass.

3. **How does selection sort compare with more advanced sorting algorithms?**

Selection sort is easier to understand and implement, but it performs much slower on large datasets because of its O(n²) time complexity. Advanced algorithms such as quicksort and mergesort use more efficient divide-and-conquer techniques that significantly reduce sorting time.

---

## Challenges Encountered

One challenge during this lab was correctly tracking the minimum value during each iteration of the sorting process. Printing the array after each pass helped verify that the algorithm was swapping elements correctly and gradually sorting the dataset as expected.
