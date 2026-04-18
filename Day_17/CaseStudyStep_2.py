import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

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

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded sucessfully...")
print("Initial entries from the dataset : ")
print(df.head())

################################################################
#   Step 2 : Data Analysis(EDA) -- exploratary data analysis
################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of Dataset : ",df.shape)
print("Column Names : ",list(df.columns))

print("Missing Values : (Per Column)")

print(df.isnull().sum())

# The below method gives info about the count of each species
print("Class Distribution : (Species Count)")
print(df["species"].value_counts())

# describe method -- give information like mean,max,min,count etc
print("Statistical Report od Dataset : ")
print(df.describe())
