# For dataset loading and unloading 
import pandas as pd
#For visualisation
import matplotlib.pyplot as plt
#For visualisation
import seaborn as sns
# For spliting data inti 4 parts and shuffling the data
from sklearn.model_selection import train_test_split
#Algorithm used to solve the case study
from sklearn.tree import DecisionTreeClassifier,plot_tree
# For last step
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
Border = "-"*50

################################################################
#   Step 1 : Load the dataset
################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "iris.csv"

# To load the dataset
df = pd.read_csv(DatasetPath)

print("Dataset gets loaded sucessfully...")
print("Initial entries from the dataset : ")
# head prints the first five data from the dataset
print(df.head())

################################################################
#   Step 2 : Data Analysis(EDA) -- exploratary data analysis
################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

# shape shows the no. of rows and columns in the dataset
print("Shape of Dataset : ",df.shape)
# colums shows the name of all the columns in the dataset by comma separated
print("Column Names : ",list(df.columns))

print("Missing Values : (Per Column)")
print(df.isnull().sum())

# The below method gives info about the count of each species
print("Class Distribution : (Species Count)")
print(df["species"].value_counts())

# describe method -- give information like mean,max,min,count etc
print("Statistical Report od Dataset : ")
print(df.describe())

################################################################
#   Step 3 : Decide Independent & Dependent Variables
################################################################

print(Border)
print("Step 3 : Decide Independent & Dependent Variables")
print(Border)

# X : Independent Variables / features
# Y : Dependent variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

################################################################
#   Step 4 : Visualisation of Dataset
################################################################

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

#ScatterPlot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Iris : Petal length vs petal width")
plt.xlabel("petal length (cm)",)
plt.ylabel("petal width (cm)",)
# legend tell about that in graph which colour is for what
plt.legend()
plt.grid(True)
plt.show()

################################################################
#   Step 5 : Split the Dataset for training and testing
################################################################

print(Border)
print("Step 5 : Split the Dataset for training and testing")
print(Border)

# Test size = 20%
# Train size = 80

X_train , X_test , Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.2,
    random_state = 42
)

print("X - Independent : ",X.shape)     # (150,4)
print("Y - Dependent: ",Y.shape)        #(150,)


print("Data spliting activity done : ")
print("X_train : ",X_train.shape)       #(120,4)
print("X_test : ",X_test.shape)         #(30,4)
print("Y_train : ",Y_train.shape)       #(120,1)
print("Y_test : ",Y_test.shape)         #(30,1)

