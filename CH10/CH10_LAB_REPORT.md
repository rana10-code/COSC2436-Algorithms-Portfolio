# Chapter 10: Greedy Algorithms (Truck Packing) — Lab Report

## Student Information
**Name:** Dhiraj Rana  
**Date:** 04/16/2026 

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**  
This algorithm is solving a packing problem, which can be classified as an optimization problem.

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**  
No, this greedy algorithm is not guaranteed to produce the optimal solution because it makes local optimal choices (packing the largest boxes first) without considering future consequences.

**What is the greedy choice made in this algorithm?**  
The greedy choice is to sort the boxes by volume in descending order and pack as many of the larger boxes as possible.

---

## Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
Sorting in descending order ensures we fit the largest boxes first, maximizing the number of boxes packed by volume.

**What would happen if we sorted the boxes in ascending order instead?**  
Sorting in ascending order would likely leave less room for larger boxes, leading to inefficient use of space.

**Why do we keep track of `used_volume`?**  
We track `used_volume` to ensure we don't exceed the truck's total volume capacity while packing.

---

## Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
Volume alone doesn't account for the actual shape and fit of boxes within the truck's dimensions.

**Give an example where a box fits by volume but not by dimensions.**  
A long, flat box might have a suitable volume but may not fit due to the length exceeding the truck's width or height.

**How would you modify the algorithm to check dimension constraints before packing a box?**  
The algorithm would need to compare each box's dimensions against the truck's (length, width, height) to verify fit before adding it.

---

## Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
The greedy approach may fail when smaller combinations of boxes actually fit better without exceeding the volume, leading to wasted space.

**How is this problem related to the Knapsack Problem?**  
It's similar to the Knapsack Problem, where items (boxes) must be selected and packed to maximize value (space) without exceeding capacity.

**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
A dynamic programming approach could guarantee an optimal solution but would be computationally expensive and slower.

**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
The algorithm would need to account for both weight and volume constraints, possibly adjusting the sorting and selection criteria.

**Why are greedy algorithms often preferred despite not always being optimal?**  
Greedy algorithms are often preferred for their simplicity and efficiency in providing good-enough solutions quickly.


## Test Results

| Input                                                        | Result                       | Notes                                |
|--------------------------------------------------------------|------------------------------|--------------------------------------|
| Truck: 5x5x5, Box: 2x2x2                                     | Box fits                     | Single box fits within the truck     |
| Truck: 5x5x5, Boxes: 2x2x2, 2x2x1                            | Both boxes fit               | Multiple boxes fit together          |
| Truck: 5x5x5, Boxes: 10x10x10                                | Box does not fit             | Single box larger than truck volume  |
| Truck: 5x5x5, Boxes: 2x2x2, 2x2x2, 2x2x2, 2x2x2, 2x2x2       | Some boxes fit              | Test edge case for volume utilization |
| Invalid Input (non-numeric/negative values)                  | Error message                | Properly handles invalid input       |


## Challenge Encountered
While implementing the pack_truck function, ensuring that boxes are packed efficiently within the truck's volume was challenging. The main issue was deciding on what basis to prioritize packing the boxes — by volume or dimensions.
Ensured the boxes were sorted by volume in descending order. This way, larger boxes were packed first, maximizing the use of space.
Considered dimension constraints to check if a box would physically fit within the truck, not just by volume.
Feel free to include any other specific challenges you faced and how you overcame them! Let me know if you need further assistance.
