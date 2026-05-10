# Chapter 12: Regression — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/30/2026
- **Course:** COSC 2436

---

## Algorithm Summary

- **How it works:**  
This lab implemented K-Nearest Neighbors (KNN) regression to predict numerical values based on nearby data points. The algorithm calculates the distance between the input sample and all training samples, selects the k closest neighbors, and averages their target values to generate a prediction.

- **Time complexity:**  
Typically O(n), where:
- n = number of training samples

- **When to use it:**  
KNN regression is useful for smaller datasets where simple, interpretable predictions are desired. It works well when similar inputs are expected to produce similar outputs.

---

## Test Results

### Program Output

```text
Bakery Data:
    weather  weekend_holiday  game_on  loaves
0         3                0        0      42
1         5                1        1      95
2         2                0        0      30
3         4                1        0      72
4         1                0        1      38
5         5                0        0      55
6         3                1        1      78
7         4                0        0      50
8         2                1        0      58
9         5                1        0      85
10        1                0        0      22
11        3                0        1      52
12        4                1        1      88
13        2                0        1      44
14        5                0        1      70
15        3                1        0      65
16        4                0        1      62
17        1                1        0      48
18        2                1        1      70
19        4                1        0      75

Features shape: (20, 3)
Target shape: (20,)

KNN model trained with k=4

Today's conditions:
Weather = 4
Weekend/Holiday = 1
Game = 0

Predicted loaves to bake: 70.5
```

### Performance Table

| Input Conditions (Weather, Weekend, Game) | Predicted Loaves | Notes |
|-------------------------------------------|------------------|-------|
| (4, 1, 0) | 70.5 | Prediction based on nearest neighboring bakery data |

---

## Reflection Questions

1. **How does KNN handle new data points?**

KNN calculates the distance from the new input point to all samples in the dataset. The algorithm identifies the k-nearest neighbors and averages their target values to produce a prediction.

2. **What challenges arise with high-dimensional data in KNN?**

High-dimensional datasets reduce the effectiveness of distance measurements because data points tend to appear similarly distant from one another. This problem, known as the “curse of dimensionality,” can reduce prediction accuracy.

3. **What preprocessing steps are important for KNN models?**

Feature scaling is extremely important because KNN relies on distance calculations. Standardization or normalization ensures that all features contribute equally instead of allowing larger numerical values to dominate the distance metric.

---

## Challenges Encountered

One challenge during this lab was implementing feature extraction while ensuring consistent input formatting for the regression model. Understanding the differences between KNN classification and KNN regression also required additional review and experimentation.

Testing the model with different input conditions helped confirm that predictions aligned with expected results and nearest-neighbor calculations.
