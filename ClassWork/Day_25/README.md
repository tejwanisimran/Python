## Day 25 : 
## Learned concepts of Bagging & Boosting in Machine Learning using case studies :
## - California Housing & 
## - Breast Cancer
---
### 📉 Case Study 1: California Housing (Regression)
- This dataset is used to predict housing prices.

### 🔹 Step 1: Individual Model (Decision Tree)
- A single decision tree is used to predict values
- Easy to understand but may overfit the data
### 👉 Learning:
- High variance problem
- Model performs well on training but not always on testing
### 🔹 Step 2: Bagging (Bootstrap Aggregation)
- Multiple decision trees are trained on different subsets of data
- Their predictions are combined (averaged)
### 👉 Learning:
- Reduces variance
- Improves stability
- Less overfitting compared to a single tree
### 🔹 Step 3: Boosting (Gradient Boosting)
- Models are trained sequentially
- Each new model focuses on correcting previous errors
### 👉 Learning:
- Reduces bias
- Builds strong models from weak learners
- More accurate but computationally intensive
---
### 📊 Case Study 2: Breast Cancer (Classification)
- This dataset is used to classify tumors as malignant or benign.
### 🔹 Step 1: Individual Model (Decision Tree)
- A basic classifier is trained
### 👉 Learning:
- Simple and interpretable
- Can overfit easily
### 🔹 Step 2: Bagging (Ensemble Classification)
- Multiple classifiers are combined
### 👉 Learning:
- Reduces overfitting
- Improves accuracy
### 🔹 Step 3: Random Forest (Advanced Bagging)
- Multiple decision trees with randomness in feature selection
### 👉 Learning:
- Better generalization
- Handles large datasets effectively
### 🔹 Step 4: Boosting (AdaBoost)
- Focuses more on misclassified data points
- Adjusts weights iteratively
### 👉 Learning:
- Improves weak classifiers
- Achieves higher accuracy step-by-step.
---
### 📈 Evaluation Metrics
- Regression:
```
Mean Squared Error (MSE)
R² Score
```
- Classification:
```
Accuracy Score
Confusion Matrix
Classification Report
```
### 👉 Learning:
- Metrics help compare models
- Essential for understanding model performance
---
### 🔥 Key Takeaway
- Bagging vs Boosting:
```
Bagging → Reduces variance (parallel learning)
Boosting → Reduces bias (sequential learning)
```
---
