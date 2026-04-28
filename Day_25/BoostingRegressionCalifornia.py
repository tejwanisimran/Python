import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
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
    # Step 4 : Create gradient boosting model
    #---------------------------------------------------------------

    boost_model = GradientBoostingRegressor(
                                                n_estimators=100,
                                                learning_rate=0.1,
                                                max_depth=3,
                                                random_state=42
        )

    #---------------------------------------------------------------
    # Step 5 : Train gradient boosting model
    #---------------------------------------------------------------

    boost_model.fit(X_train,Y_train)

    #---------------------------------------------------------------
    # Step 6 :Test gradient boosting model
    #---------------------------------------------------------------

    Y_pred = boost_model.predict(X_test)

    #---------------------------------------------------------------
    # Step 7 : Evaluate the gradient boosting model
    #---------------------------------------------------------------

    print(Border)
    print("Step 7 : Evaluate the bagging model")
    print(Border)

    print("Mean Squared Error : ",mean_squared_error(Y_test,Y_pred))
    print("R Square : ",r2_score(Y_test,Y_pred))


if __name__ == "__main__":
    main()