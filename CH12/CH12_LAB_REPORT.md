# Chapter 12: Regression — Lab Report

## Student Information
- **Name:** Dhiraj Rana
- **Date:** 04/30/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** KNN regression predicts a target value by identifying the k closest samples in the dataset to the input point and averaging their target values. It's a non-parametric, lazy learning algorithm.
- **Time complexity:** Typically O(n), where n is the number of samples in the dataset.
- **When to use it:** Suitable for smaller datasets where interpretability and simplicity are important.

## Test Results

| Input Conditions (Weather, Weekend, Game) | Predicted Loaves | Notes |
|-------------------------------------------|------------------|-------|
| (4, 1, 0)                                 | 70.5             | Matches expected output based on similar historical data |

## Reflection Questions

1. **How does KNN handle new data points?**
   KNN calculates distances from the new point to all dataset points, finds the k-nearest neighbors, and averages their values to make a prediction.

2. **What challenges arise with high-dimensional data in KNN?**
   High-dimensional data can dilute the significance of distance measures, leading to poor predictions due to the "curse of dimensionality."

3. **What preprocessing steps are essential for KNN models?**
   Feature scaling is critical to ensure all features contribute equally to distance calculations; techniques like standardization or normalization are recommended.

## Challenges Encountered
Implementing the feature extraction process to ensure consistent data shape was challenging. Understanding differences between classification and regression in KNN required reviewing resources. Testing confirmed model predictions aligned with manual calculations.
