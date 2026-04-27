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
    # Step 2 : Select Features(Independent)
    #---------------------------------------------------------------
    
    print(border)
    print("Step 2 : Select Features(Independent)")
    print(border)

    X = df[["AnnualIncome" , "SpendingScore"]]

    print("Selected fetaures : ")
    print(X.head())

    print("Shape of selected features : ")
    print(X.shape)

    #---------------------------------------------------------------
    # Step 3 : Scale the data
    #---------------------------------------------------------------
    
    print(border)
    print("Step 3 : Scale the data")
    print(border)
    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    print('Data after scalling is : ')
    print(X_scaled[:5])

    
    #---------------------------------------------------------------
    # Step 4 : Use elbow method
    #---------------------------------------------------------------
    
    print(border)
    print("Step 4 : Use elbow method")
    print(border)

    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters=i , random_state=42 , n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11) , WCSS , marker= 'o')
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.grid(True)
    plt.show()

    #---------------------------------------------------------------
    # Step 5 : Train the model
    #---------------------------------------------------------------
    
    print(border)
    print("Step 5 : Train the model")
    print(border)

    model = KMeans(n_clusters=4 , random_state=42 , n_init=10)
    Clusters = model.fit_predict(X_scaled)

    df["Clusters"] = Clusters

    print("Dataset with cluster : ")
    print(df.head(30))

if __name__ == "__main__":
    main()