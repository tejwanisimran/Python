import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error , r2_score

def main():
    Border = "="*70

    #---------------------------------------------------------------
    # Step 1 : Load the data
    #---------------------------------------------------------------
    print(Border)
    print("Step 1 : Load the data")
    print(Border)

    df = pd.read_csv("california_housing.csv")
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

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    #---------------------------------------------------------------
    # Step 4 : Create base model
    #---------------------------------------------------------------

    base_model = DecisionTreeRegressor(random_state=42)

    #---------------------------------------------------------------
    # Step 5 : Create bagging model
    #---------------------------------------------------------------

    bagging_model = BaggingRegressor(
                                        estimator = base_model,
                                        n_estimators = 10,
                                        random_state=42
    )

    #---------------------------------------------------------------
    # Step 6 : Train bagging model
    #---------------------------------------------------------------

    bagging_model.fit(X_train,Y_train)

    #---------------------------------------------------------------
    # Step 7 :Test bagging model
    #---------------------------------------------------------------

    Y_pred = bagging_model.predict(X_test)

    #---------------------------------------------------------------
    # Step 8 : Evaluate the bagging model
    #---------------------------------------------------------------

    print(Border)
    print("Step 8 : Evaluate the bagging model")
    print(Border)

    print("Mean Squared Error : ",mean_squared_error(Y_test,Y_pred))
    print("R Square : ",r2_score(Y_test,Y_pred))


if __name__ == "__main__":
    main()