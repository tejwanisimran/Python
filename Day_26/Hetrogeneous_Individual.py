
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score , confusion_matrix , classification_report

#====================================================
# Step 1 : Load the dataset
#====================================================
Border = "="*40

print(Border)
print("Step 1 : Load the dataset")
print(Border)

data = load_breast_cancer()

X = data.data
Y = data.target

print("Shape of Independent variables : ",X.shape)
print("Shape of Dependent variables : ",Y.shape)

#====================================================
# Step 2 : Split the dataset
#====================================================

print(Border)
print("Step 2 : Split the dataset")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

print("X_train : ",X_train.shape)      
print("X_test : ",X_test.shape)         
print("Y_train : ",Y_train.shape)       
print("Y_test : ",Y_test.shape)

#====================================================
# Step 3 : Create base models
#====================================================

print(Border)
print("Step 3 : Create base models")
print(Border)

model_lr = LogisticRegression(max_iter=5000)

model_dt = DecisionTreeClassifier(random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)

print("Base models created")

#====================================================
# Step 4 : Train base models
#====================================================

print(Border)
print("Step 4 : Train base models")
print(Border)

model_lr.fit(X_train,Y_train)
model_dt.fit(X_train,Y_train)
model_knn.fit(X_train,Y_train)

print("Models trained")

#====================================================
# Step 5 : Calculate individual accuracy
#====================================================

print(Border)
print("Step 5 : Calculate individual accuracy")
print(Border)

pred_lr = model_lr.predict(X_test)
pred_dt = model_dt.predict(X_test)
pred_knn = model_knn.predict(X_test)

acc_lr = accuracy_score(pred_lr,Y_test)
acc_dt = accuracy_score(pred_dt,Y_test)
acc_knn = accuracy_score(pred_knn,Y_test)

print("Individual model accuracy : ")
print("Logistic Regression : ",acc_lr)
print("Decission Tree : ",acc_dt)
print("KNN :  ",acc_knn)

