## Day 24 : 
## Solved Case Study (Mall_Customers) with Industrial steps.

## This case study applies K-Means Clustering (Unsupervised Learning) to segment mall customers based on their spending behavior.
---
### Learned concepts like : 
---
### 1. Data Loading
- Loading dataset using Pandas
- Understanding dataset structure (rows, columns, missing values)
---
### 2. Feature Selection
- Selecting important features:
```
- Annual Income
- Spending Score
```
- Ignoring irrelevant columns for clustering
---
### 3. Data Scaling
- Applying StandardScaler for normalization
- Important for distance-based algorithms like K-Means
---
### 4. Elbow Method
- Using Elbow Method to find optimal number of clusters
- Plotting:
```
Number of clusters vs WCSS (Within Cluster Sum of Squares)
```
---
### 5. K-Means Clustering
- Applying KMeans algorithm
- Assigning cluster labels to each data point
- Grouping customers into clusters.
---
### 6. Model Output
- Adding cluster column to dataset
- Understanding different customer segments
---
