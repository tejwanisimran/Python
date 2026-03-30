import os
import sys

def DirectoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory...")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory...")
        return
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName,SubFolder,FileName,in os.walk(DirName):        
        for fName in FileName:
            FileCount += 1
            fName = os.path.join(FolderName , fName)
            print("FileName : ",fName)
            print("FileSize : ",os.path.getsize(fName))     
            if(os.path.getsize(fName) == 0):        # Empty File
                EmptyFileCount += 1
                os.remove(fName)

    Border = "-"*50
    print(Border)
    print("----------------Automation Report-----------------")
    print("Total Files scanned : ",FileCount)
    print("Total empty Files Found : ",EmptyFileCount)
    print(Border)

def main():
    Border = "-"*50
    print(Border)
    print("----------Marvellous Directory Automation---------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments...")
        print("Please specify the name of directory...")
        return 
    
    DirectoryScanner(sys.argv[1])

    print(Border)
    print("----------Marvellous Directory Automation---------")
    print(Border)


if __name__ =="__main__":
    main()