import pandas as pd

def main():

    Data = {
        "Name" : ["Sagar","Amit","Pooja"],
        "Age" : [23,25,26],
        "City" : ["Pune","Mumbai","Satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj)


if __name__ == "__main__":
    main()