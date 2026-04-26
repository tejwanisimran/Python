import pandas as pd
import numpy as np

import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix  

#-----------------------------------------------------------------------
# Function Name : DisplayInfo
# Description : It displays the formated title
# Parameters : title(str)
# Return : None
# Date : 14/03/2026
# Author : Simran Naveen Tejwani
#-----------------------------------------------------------------------
def DisplayInfo(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)

#-----------------------------------------------------------------------
# Function Name : ShowData
# Description : It shows the basic information about dataset
# Parameters : df 
#              df -> pandas dataframe object 
#              message
#              message -> Heading text to display
# Return : None
# Date : 14/03/2026
# Author : Simran Naveen Tejwani
#-----------------------------------------------------------------------
def ShowData(df , message):
    DisplayInfo(message)

    print("\nFirst five rows of the dataset : ")
    print(df.head())

    print("\nShape of the dataset : ")
    print(df.shape)

    print("\nColumns name : ")
    print(df.columns.tolist())

    print("\nMissing values in the dataset : ")
    print(df.isnull().sum())

#-----------------------------------------------------------------------
# Function Name : MarvellousTitanicLogistic
# Description : This is the main pipeline cntroller.
#               It loads the dataset , shows the raw data.
#               It preprocess the dataset & train the model.
# Parameters : DataPath of the dataset file
# Return : None
# Date : 14/03/2026
# Author : Simran Naveen Tejwani
#-----------------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")

    df = pd.read_csv(DataPath)

    ShowData(df , "Initial dataset")

#-----------------------------------------------------------------------
# Function Name : main
# Description : Starting point of the application
# Parameters : None
# Return : None
# Date : 14/03/2026
# Author : Simran Naveen Tejwani
#-----------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")


if __name__ == "__main__":
    main()