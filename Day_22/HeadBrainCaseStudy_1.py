# pandas for loading the data
import pandas as pd
# numpy for mathematical calculations
import numpy as np
# sklearn.model_selection for spliting the data set for training & testing
from sklearn.model_selection import train_test_split
# sklearn.linear_model for importing the Linear Regression class
from sklearn.linear_model import LinearRegression
# matplotlib.pyplot for visualisation
import matplotlib.pyplot as plt
# sklearn.metrics for importing in build functions for calculating error rate  
from sklearn.metrics import mean_squared_error , r2_score

def MarvellousHeadBrain():
    border = "-"*70

    #-------------------------------------------------------------
    # Step 1 : Load the data set
    #-------------------------------------------------------------

    print(border)
    print("Step 1 : Load the data set")
    print(border)

    df = pd.read_csv("MarvellousHeadBrain.csv")

    print("Few records from the data set")
    # head is used to display the first 5 records of the data set.
    print(df.head())

    
    #-------------------------------------------------------------
    # Step 2 : Check missing values
    #-------------------------------------------------------------

    print(border)
    print("Step 2 : Check missing values")
    print(border)

    print("Missing values in the data set : ")
    # isnull is used to check whether there are any missing values or not 
    print(df.isnull().sum())

    #-------------------------------------------------------------
    # Step 3 : Displaying statistical summary
    #-------------------------------------------------------------

    print(border)
    print("Step 3 : Displaying statistical summary")
    print(border)

    print("Statistical summary of the data : ")
    # describe is used to display the statistical summary of the data set like (mean,max,std,etc)
    print(df.describe())

    #-------------------------------------------------------------
    # Step 4 : Co-relation between columns
    #-------------------------------------------------------------

    print(border)
    print("Step 4 : Co-relation between columns")
    print(border)

    print("Co-relation matrix : ")
    # corr() is used to tell Co-relation between between the columns.
    print(df.corr())

    #-------------------------------------------------------------
    # Step 5 : Spliting the dataset into independent & dependent variables
    #-------------------------------------------------------------

    print(border)
    print("Step 5 : Spliting the dataset into independent & dependent variables")
    print(border)

    X = df[['Gender' , 'Age Range' , 'Head Size(cm^3)' ]]
    Y = df['Brain Weight(grams)']

    print("Shape of the independent variables : ",X.shape)
    print("Shape of the dependent variables : ",Y.shape)

    #-------------------------------------------------------------
    # Step 6 : Spliting the data for training & testing
    #-------------------------------------------------------------

    print(border)
    print("Step 6 : Spliting the data for training & testing")
    print(border)

    X_train ,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #-------------------------------------------------------------
    # Step 7 : Create & train the model
    #-------------------------------------------------------------

    print(border)
    print("Step 7 : Create & train the model")
    print(border)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    #-------------------------------------------------------------
    # Step 8 : Test the model
    #-------------------------------------------------------------

    print(border)
    print("Step 8 : Test the model")
    print(border)

    Y_pred = model.predict(X_test)

    #-------------------------------------------------------------
    # Step 9 : Evaluate the model
    #-------------------------------------------------------------

    print(border)
    print("Step 9 : Evaluate the model")
    print(border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    r2 = r2_score(Y_test,Y_pred)

    print("Mean squared error : ",MSE)
    print("Root Mean squared error : ",RMSE)
    print("Rsquare value : ",r2)

    #-------------------------------------------------------------
    # Step 10 : Calculating the model co-efficient & intercept
    #-------------------------------------------------------------

    print(border)
    print("Step 10 : Calculating the model co-efficient")
    print(border)

    
    print(border)
    print("Step 11 : Calculate model coefficient")
    print(border)

    for column , value in zip(X.columns , model.coef_):
        print(f"{column} : {value}")

    print("Intercept : ",model.intercept_)

    #-------------------------------------------------------------
    # Step 11 : Compare actual & predicted values
    #-------------------------------------------------------------

    print(border)
    print("Step 11 : Compare actual & predicted values")
    print(border)

    Result = pd.DataFrame({'Actual sale ': Y_test.values,'Predicted sale ': Y_pred})

    print(Result.head(10))

    #-------------------------------------------------------------
    # Step 12 : Plot actual v/s predicted
    #-------------------------------------------------------------

    print(border)
    print("Step 13 : Plot actual v/s predicted")
    print(border)

    plt.figure(figsize=(8,5))       # grid size

    plt.scatter(Y_test,Y_pred)      # to plot scatter plot

    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")

    plt.title("Actual head weight v/s Predicted head weight")

    plt.grid(True)
    plt.show()

def main():
    MarvellousHeadBrain()

if __name__ == "__main__":
    main()