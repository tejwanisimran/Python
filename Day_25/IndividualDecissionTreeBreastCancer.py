import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix

def main():
    Border = "="*40

    #---------------------------------------------------------------
    # Step 1 : Load the data
    #---------------------------------------------------------------
    print(Border)
    print("Step 1 : Load the data")
    print(Border)

    df = pd.read_csv("breast_cancer.csv")
    print("Shape of the dataset : ",df.shape)
    print("First five records are : ",df.head())

    #---------------------------------------------------------------
    # Step 2 : Separate features & labels
    #---------------------------------------------------------------

    X = df.drop("target",axis=1)
    Y = df["target"]

    #---------------------------------------------------------------
    # Step 3 : Split the dataset for training & testing
    #---------------------------------------------------------------

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    #---------------------------------------------------------------
    # Step 4 : Create model
    #---------------------------------------------------------------

    model = DecisionTreeClassifier(random_state=42)

    #---------------------------------------------------------------
    # Step 5 : Train model
    #---------------------------------------------------------------

    model.fit(X_train,Y_train)

    #---------------------------------------------------------------
    # Step 6 :Test model
    #---------------------------------------------------------------

    Y_pred = model.predict(X_test)

    #---------------------------------------------------------------
    # Step 7 : Evaluate the bagging model
    #---------------------------------------------------------------

    print("Accuracy : ",accuracy_score(Y_test,Y_pred))

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test,Y_pred))

if __name__ == "__main__":
    main()