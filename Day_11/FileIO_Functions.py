import os

def main():
    FileName = input("Enter the name of file : ")
    if(os.path.exists(FileName)):
        fobj = open(FileName , "r")

        print(fobj.name)    # Demo.txt
        print(fobj.mode)    # r
        print(fobj.closed)  # False
        fobj.close()
        print(fobj.closed)  # True
    else :
        print("Error : There is no such file or directory...")

if __name__ == "__main__":
    main()