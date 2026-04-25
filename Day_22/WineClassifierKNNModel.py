import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

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

    #--------------------------------------------------------------------------
    # Step 4 : Split the data for training & testing
    #--------------------------------------------------------------------------

    print(border)
    print("Step 4 : Split the data for training & testing")
    print(border)

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Information of training & testing : ")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #--------------------------------------------------------------------------
    # Step 5 : Feature scaling
    #--------------------------------------------------------------------------

    print(border)
    print("Step 5 : Feature scaling")
    print(border)

    scalar = StandardScaler()
    # Independent scaling
    X_trained_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Features scaling is done...")

    #--------------------------------------------------------------------------
    # Step 6 : Explore the multiple values of k
    #           Hyper Parameter tuning (k)
    #--------------------------------------------------------------------------

    print(border)
    print("Step 6 : Explore the multiple values of k")
    print(border)

    accuracy_scores = []

    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_trained_scaled , Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)

        accuracy_scores.append(accuracy)

        print(border)
        print("Accuracy report of all K values from 1 to 20 : ")

        for value in accuracy_scores :
                print(value)

        print(border)

def main():
    border = "-"*40
    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousWinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()