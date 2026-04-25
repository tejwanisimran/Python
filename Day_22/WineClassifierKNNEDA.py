import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousWinePredictor(DataPath):
    border = "-"*70

    #--------------------------------------------------------------------------
    # Step 1 : Load the data ste from the CSV file
    #--------------------------------------------------------------------------

    print(border)
    print("Step 1 : Load the data ste from the CSV file")
    print(border)

    df = pd.read_csv(DataPath)
    print(border)
    print("Few Record from the data set : ")
    print(df.head())
    print(border)

    #--------------------------------------------------------------------------
    # Step 2 : Clean the dataset by removing empty rows
    #--------------------------------------------------------------------------

    print(border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(border)

    df.dropna(inplace = True)

    print("Total records : ",df.shape[0])
    print("Total coumns : ",df.shape[1])
    print(border)

    #--------------------------------------------------------------------------
    # Step 3 : Separate independent & dependent varaibles
    #--------------------------------------------------------------------------

    print(border)
    print("Step 3 : Separate independent & dependent varaibles")
    print(border)

    X = df.drop(columns= ['Class'])
    Y = df['Class']

    print("Shape of independent varaibles : ",X.shape)
    print("Shape of dependent varaibles : ",Y.shape)

    print(border)
    print("Input columns : ",X.columns.to_list())
    print("Output Columns : Class")

def main():
    border = "-"*40
    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousWinePredictor("WinePredictor.csv")



if __name__ == "__main__":
    main()