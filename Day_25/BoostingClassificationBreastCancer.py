import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
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

    X = df.drop("target",axis=1)
    Y = df["target"]

    #---------------------------------------------------------------
    # Step 3 : Split the dataset for training & testing
    #---------------------------------------------------------------

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    #---------------------------------------------------------------
    # Step 4 : Create boosting model (AdaBoost)
    #---------------------------------------------------------------

    boost_model = AdaBoostClassifier(
                                        n_estimators=50,
                                        learning_rate=1.0,
                                        random_state=42
        )

    #---------------------------------------------------------------
    # Step 5 : Train boosting model
    #---------------------------------------------------------------

    boost_model.fit(X_train,Y_train)

    #---------------------------------------------------------------
    # Step 6 :Test boosting model
    #---------------------------------------------------------------

    Y_pred = boost_model.predict(X_test)

    #---------------------------------------------------------------
    # Step 7 : Evaluate the bagging model
    #---------------------------------------------------------------

    print("boosting Accuracy : ",accuracy_score(Y_test,Y_pred))

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test,Y_pred))

if __name__ == "__main__":
    main()