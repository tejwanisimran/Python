import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix

def main():
    Border = "="*70

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
    print(Border)
    print("Step 2 : Separate features & labels")
    print(Border)
    

    X = df.drop("target",axis=1)
    Y = df["target"]

    print("Shape of Independent Variables : ",X.shape)
    print("Shape of Dependent Variables : ",Y.shape)

    #---------------------------------------------------------------
    # Step 3 : Split the dataset for training & testing
    #---------------------------------------------------------------
    print(Border)
    print("Step 3 : Split the dataset for training & testing")
    print(Border)
    

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train : ",X_train.shape)      
    print("X_test : ",X_test.shape)         
    print("Y_train : ",Y_train.shape)       
    print("Y_test : ",Y_test.shape)    

    #---------------------------------------------------------------
    # Step 4 : Create randomforest model
    #---------------------------------------------------------------
    print(Border)
    print("Step 4 : Create randomforest model")
    print(Border)

    rf_model = RandomForestClassifier(
                                        n_estimators=100,
                                        random_state=42
    )

    #---------------------------------------------------------------
    # Step 5 : Train bagging model
    #---------------------------------------------------------------

    print(Border)
    print("Step 5 : Train bagging model")
    print(Border)

    rf_model.fit(X_train,Y_train)

    #---------------------------------------------------------------
    # Step 6 :Test bagging model
    #---------------------------------------------------------------
    print(Border)
    print("Step 6 :Test bagging model")
    print(Border)

    Y_pred = rf_model.predict(X_test)

    #---------------------------------------------------------------
    # Step 7 : Evaluate the bagging model
    #---------------------------------------------------------------

    print(Border)
    print("SStep 7 : Evaluate the bagging model")
    print(Border)

    print("Bagging Accuracy : ",accuracy_score(Y_test,Y_pred))

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test,Y_pred))

if __name__ == "__main__":
    main()