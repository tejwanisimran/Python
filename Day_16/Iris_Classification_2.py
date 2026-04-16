from sklearn.datasets import load_iris

def main():
    print("Iris Classification case study")

    Dataset = load_iris()

    # Metadata of Dataset 
    print("Independent Variables are : ")
    print(Dataset.feature_names)

    print("Dependent varaibles are : ")
    print(Dataset.target_names)



if __name__ == "__main__":
    main()

