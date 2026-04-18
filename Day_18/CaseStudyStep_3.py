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

