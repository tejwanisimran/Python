## Day 3 : 
## Solved case study (Titanic) with industrial steps.
---
### Learned concepts like : 
---
### 1. Data Loading
- Loading dataset using Pandas
- Understanding dataset structure (columns, shape, missing values)
---
### 2. Data Preprocessing
- Removing unnecessary columns:
```
PassengerId
Name
Cabin
```
- Handling missing values:
```
Age → replaced with median
Fare → replaced with median
Embarked → replaced with mode
```
---
### 3. Data Cleaning & Transformation
- Converting text data into numeric values
- Encoding categorical variables using one-hot encoding
- Converting boolean values to integers
---
### 4. Feature Selection
- Independent variables (X): Passenger features
- Dependent variable (Y): Survival status
---
### 5. Data Splitting
- Splitting dataset into:
```
Training set
Testing set
```
- Using train_test_split() for model validation
---
### 6. Model Building
- Using Logistic Regression for classification
- Training model using .fit()
---
### 7. Model Evaluation
- Accuracy Score
- Confusion Matrix
---
### 8. Model Persistence
- Saving trained model using joblib
- Loading model for future predictions
---
### 9. Model Interpretation
- Understanding:
 ```
- Model coefficients
- Intercept values
```
---
