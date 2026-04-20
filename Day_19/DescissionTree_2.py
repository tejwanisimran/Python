# This is used to load the dataset i.e iris
from sklearn.datasets import load_iris
# Used for spliting the dataset
from sklearn.model_selection import train_test_split
#This is used to import the DecissionTreeClassifier class
from sklearn.tree import DecisionTreeClassifier
#This is used to import for calculating the accuracy
from sklearn.metrics import accuracy_score
# Used for visualisation
from sklearn.tree import plot_tree
# Used for visualisation
import matplotlib.pyplot as plt


def main():
    iris = load_iris()

    # These are Independent Variables
    X = iris.data
    # These are Dependent Variables
    Y = iris.target
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2) 

    model = DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",accuracy*100)

    # Visualization

    plt.figure(figsize=(12,8))

    plot_tree(model,filled = True , feature_names = iris.feature_names , class_names = iris.target_names)

    plt.title("Marvellous DecissionTreeClassifier")

    plt.show()

if __name__ == "__main__":
    main()