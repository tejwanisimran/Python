import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#-----------------------------------------------------------------------
# Function Name : main
# Description   : Starting point of the application
# Parameters    : None
# Return        : None
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------

def main():
    border = "="*70
    #---------------------------------------------------------------
    # Step 1 : Load the dataset
    #---------------------------------------------------------------
    print(border)
    print("Step 1 : Load the dataset")
    print(border)
    df = pd.read_csv("Mall_Customers.csv")

    print("First few records : ")
    print(df.head())

    print("Shape of the dataset : ")
    print(df.shape)

    print("Missing values in the dataset : ")
    print(df.isnull().sum())

    #---------------------------------------------------------------
    # Step 1 : Load the dataset
    #---------------------------------------------------------------
    
    print(border)
    print("Step 2 : Select Features(Independent)")
    print(border)

    X = df[["AnnualIncome" , "SpendingScore"]]

    print("Selected fetaures : ")
    print(X.head())

    print("Shape of selected features : ")


if __name__ == "__main__":
    main()