import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error ,r2_score

def MarvellousAdvertising(DataPath):
    Border = "-"*60
    #-----------------------------------------------------------------
    # Step 1 : Load the data set
    #-----------------------------------------------------------------

    print(Border)
    print("Step 1 : Load the data set")
    print(Border)

    df = pd.read_csv(DataPath) 

    print("Few records from the dataset : ")
    print(df.head())

    #-----------------------------------------------------------------
    # Step 2 : Remove unwanted columns
    #-----------------------------------------------------------------

    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    print("Shape of the dataset berfor removal : ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'],inplace = True)

    print("Shape of the dataset after removal : ",df.shape)
    
    print(Border)
    print("Clean dataset is : ")
    print(Border)

    print(df.head())

    #-----------------------------------------------------------------
    # Step 3 : Check missing values
    #-----------------------------------------------------------------

    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Missing values count : ")
    print(df.isnull().sum())

    #-----------------------------------------------------------------
    # Step 4 : Display statistical summary
    #-----------------------------------------------------------------

    print(Border)
    print("Step 4 : Display statistical summary")
    print(Border)

    print(df.describe())

    #-----------------------------------------------------------------
    # Step 5 : Co-relation between columns
    #-----------------------------------------------------------------

    print(Border)
    print("Step 5 : Co-relation between columns")
    print(Border)

    print("Co-relation matrix : ")
    print(df.corr())

def main():

   MarvellousAdvertising("Advertising.csv")

if __name__ == "__main__":
    main()