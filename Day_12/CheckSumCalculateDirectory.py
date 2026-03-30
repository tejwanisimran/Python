import hashlib
import os

def CalculateCheckSum(Filename):
    fobj = open(Filename , "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()     # haichyane CheckSum mildto

def DirectoryWatcher(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        return 
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fName in FileName:
            fName = os.path.join(FolderName,fName)
            CheckSum = CalculateCheckSum(fName)
            print(f"FileName : {fName} , CheckSum : {CheckSum}")



def main():
    DirectoryWatcher()
    

if __name__ == "__main__":
    main()