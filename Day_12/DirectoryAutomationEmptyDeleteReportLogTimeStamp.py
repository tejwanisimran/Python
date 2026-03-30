import os
import sys
import time

def DirectoryScanner(DirName = "Marvellous"):
    Border = "-"*50
    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Cleaner Script\n")

    fobj.write(Border+"\n")

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
            if(os.path.getsize(fName) == 0):        # Empty File
                EmptyFileCount += 1
                os.remove(fName)

    fobj.write("Total Files scanned : "+str(FileCount)+"\n")
    fobj.write("Total Empty Files Found : "+str(EmptyFileCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

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