import pandas as pd
import numpy as np

import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix  

#-----------------------------------------------------------------------
# Function Name : LOadPreservedModel
# Description   : It is used to load the preserved model
# Parameters    : model 
# Return        : filename
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------

def LoadPreservedModel(filename):

    loaded_model = joblib.load(filename)

    print("Model Loaded sucessfully...")

    return loaded_model

#-----------------------------------------------------------------------
# Function Name : PreserveModel
# Description   : It is used to preserve the model on secondary storage
# Parameters    : model , filename
# Return        : None
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------
def PreserveModel(model , filename):

    joblib.dump(model,filename)

    print("\nModel preserved sucessfully with name : ",filename)


#-----------------------------------------------------------------------
# Function Name : TrainTitanicModel
# Description   : It does splitting of X,Y,training data , testing data
# Parameters    : df
#                 df -> dataframe
# Return        : None
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------

def TrainTitanicModel(df):
    
    # Spilt the features & labels
    X = df.drop("Survived" , axis= 1)
    Y = df["Survived"]

    print("\nFeatures : ")
    print(X.head())

    print("\nLabels : ")
    print(Y.head())

    print("\nShape of X : ",X.shape)
    print("\nShape of Y : ",Y.shape)

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2 , random_state=42)

    print("\nShape of X_train : ",X_train.shape)
    print("\nShape of X_test : ",X_test.shape)
    print("\nShape of Y_train : ",Y_train.shape)
    print("\nShape of Y_test : ",Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train,Y_train)

    print("\nModel trained sucessfully...")
    print("\nIntercept of model : ")
    print(model.intercept_)

    print("\nCo-efficient of model : ")
    for feature,coefficient in zip(X.columns , model.coef_[0]):
        print(feature , " : " , coefficient)

    PreserveModel(model , "MarvellousTitanic.pkl")

    loaded_model = LoadPreservedModel("MarvellousTitanic.pkl")

    Y_Pred = loaded_model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_Pred)

    print("Accuracy is : ",accuracy)

    cm = confusion_matrix(Y_test,Y_Pred)

    print("Confusion matrix is : ")
    print(cm)

    
#-----------------------------------------------------------------------
# Function Name : DisplayInfo
# Description   : It displays the formated title
# Parameters    : title(str)
# Return        : None
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------
def DisplayInfo(title):
    print("\n" + "="*90)
    print(title)
    print("="*90)

#-----------------------------------------------------------------------
# Function Name : ShowData
# Description   : It shows the basic information about dataset
# Parameters    : df 
#                 df -> pandas dataframe object 
#                 message
#                 message -> Heading text to display
# Return        : None
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
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
# Description   : It does preprocessing
#                 It removes unnecessary columns
#                 It handles missing values
#                 It converts text data to numeric value
#                 It does encoding to catagorical columns
# Parameters    : df
#                 df -> Pandas dataframe
# Return        : df
#                 df -> Cleaned pandas dataframe
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------
def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original data")

    print(df.head())

    # Remove unnecessary columns : 
    drop_columns = ["Passengerid" , "zero" , "Name" , "Cabin"]

    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\n Columns to be droped : ")

    print(existing_columns)

    # drop the unwanted columns : 

    df = df.drop(columns = existing_columns)

    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    # Handle age column : 

    if "Age" in df.columns : 
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        # Invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"] , errors="coerce")

        age_median = df["Age"].median()

        # Relace missing values with median

        df["Age"] = df["Age"].fillna(age_median)

        print("Each column after processing : ")

        print(df["Age"].head(10))

    # Handle Fare column

    if "Fare" in df.columns : 
        print("\nFare column before preprocessing")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"] , errors="coerce")

        fare_median = df["Fare"].median()

        # Relace missing values with median

        df["Fare"] = df["Fare"].fillna(fare_median)
        print("\nMedian of fare column is : ",fare_median)

        print("Each column after processing : ")

        print(df["Fare"].head(10))

    # HAndle Embarked column : 

    if "Embarked" in df.columns:
        print("\nEmbarked column before preprocessing")
        print(df["Embarked"].head(10))

        # COnver the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Removing missing values : 
        df["Embarked"] = df["Embarked"].replace(['nan' , 'None' , ''] , np.nan)

        # Get modt frequent value
        embarked_mode = df["Embarked"].mode()[0]

        print("\nMode of Embarked column : ",embarked_mode)
        
        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("Embarked column after preprocessing")
        print(df["Embarked"].head(10))

    # Handle Sex column

    if "Sex" in df.columns : 
        print("\nSex column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"] , errors="coerce")

        print("Sex column after preprocessing")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing")

    print(df.head())    

    print("\nMissing values after preprocessing ")
    print(df.isnull().sum())

    # Encode embarked column
    df = pd.get_dummies(df,columns=["Embarked"] , drop_first=True)

    print("\nData after encoding : ")
    print(df.head())
    print("Shape of the dataset : ",df.shape)

    # convert boolean columns into integer

    for col in df.columns : 
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\nData after encoding : ")
    print(df.head())
    print("Shape of the dataset : ",df.shape)
    
    return df

#-----------------------------------------------------------------------
# Function Name : MarvellousTitanicLogistic
# Description   : This is the main pipeline cntroller.
#                 It loads the dataset , shows the raw data.
#                 It preprocess the dataset & train the model.
# Parameters    : DataPath of the dataset file
# Return        : None
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")

    df = pd.read_csv(DataPath)

    ShowData(df , "Initial dataset")
    df = CleanTitanicData(df)

    TrainTitanicModel(df)


#-----------------------------------------------------------------------
# Function Name : main
# Description   : Starting point of the application
# Parameters    : None
# Return        : None
# Date          : 14/03/2026
# Author        : Simran Naveen Tejwani
#-----------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")


if __name__ == "__main__":
    main()