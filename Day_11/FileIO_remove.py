
import os

def main():
    FileName = input("Enter the name of file : ")
    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("File gets deleted...")
    else :
        print("Error : There is no such file or directory...")

if __name__ == "__main__":
    main()