# This is used to load the dataset i.e iris
from sklearn.datasets import load_iris
# Used for spliting the dataset
from sklearn.model_selection import train_test_split
#This is used to import the KNeighborsClassifier class
from sklearn.neighbors import KNeighborsClassifier
#This is used to import accuracy_score method for calculating the accuracy
from sklearn.metrics import accuracy_score

def main():
    iris = load_iris()

    # These are Independent Variables
    X = iris.data
    # These are Dependent Variables
    Y = iris.target

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2) 

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",accuracy*100)


if __name__ == "__main__":
    main()