## Day 22 :
## Solved Case Study (Wine Predictor) using Industrial steps.
## This case study implements a Machine Learning classification model using the K-Nearest Neighbors (KNN) algorithm to classify wine types based on their chemical properties.
---
### Learned concepts like : 
---
### 1. Data Loading & Cleaning
- Loading dataset using Pandas
- Removing missing values using dropna()
- Understanding dataset structure and features
---
### 2. Feature Selection
- Independent variables (X): All input features
- Dependent variable (Y): Wine Class
- Separating features and labels
---
### 3. Data Splitting
- Splitting dataset into:
```
Training set
Testing set
```
- Using train_test_split() with stratification
---
### 4. Feature Scaling
- Applying StandardScaler for normalization
- Important for distance-based algorithms like KNN
---
### 5. KNN Model Implementation
- Using KNeighborsClassifier from Scikit-learn
- Training model using .fit()
- Predicting using .predict().
---
### 6. Hyperparameter Tuning
- Testing multiple values of K (1 to 20)
- Selecting best K based on accuracy
---
### 7. Visualization
- Plotting graph:
- K vs Accuracy
- Understanding model performance visually.
---
### 8. Model Evaluation
- Accuracy Score
- Confusion Matrix
- Classification Report
---
