## Day 26 : 
## Learnt algorithm Support Vector Machine(SVM) & concept of voting classifier in Machine Learning using case study of Breast Cancer.
---
### 🔹 1. Support Vector Machine (SVM)
- Support Vector Machine is a supervised learning algorithm used for classification.

### ✔️ Key Idea:
- Finds the optimal hyperplane that separates data into classes
- Maximizes the margin between different classes
### ✔️ Important Parameters:
- kernel = 'rbf' → Handles non-linear data
- C → Controls margin (regularization)
- gamma → Controls influence of data points
### ✔️ Learning Outcomes:
- Works well for high-dimensional data
- Effective for both linear and non-linear classification
- Sensitive to parameter tuning
---
### 🔹 2. Voting Classifier (Ensemble Learning)
- Voting Classifier combines predictions from multiple models to improve accuracy.

### ✔️ Base Models Used:
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
---
### * Hard Voting
- Final prediction is based on majority voting
- Each model gives one vote
### 👉 Learning:
- Simple and effective
- Works well when models are diverse
---
### * Soft Voting
- Uses probability predictions
- Chooses class with highest average probability
### 👉 Learning:
- More accurate than hard voting (in most cases)
- Requires models that support probability prediction
---
