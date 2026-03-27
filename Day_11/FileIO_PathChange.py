# isabs() is used to check whether the path is absolute path or not
# abspath() is used to give the absolute path of the given file
# this is a blind path because they dont see whether the file exists 
# or not so put exists method to check whether the file exists or not
import os

def main():
    FileName = input("Enter the name of file : ")
    if(os.path.exists(FileName)):
        Ret = os.path.isabs(FileName)

        if(Ret == True):
            print("It is absolute path...")
        else:
            print("It is relative path...")

        new_path = os.path.abspath(FileName)

        print("Updated path : ",new_path)
    else :
        print("Error : There is no such file or directory...")

if __name__ == "__main__":
    main()