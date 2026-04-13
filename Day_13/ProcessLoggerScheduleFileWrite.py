import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-"*70

    Ret = False

    Ret = os.path.exists(FolderName)
    
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create the folder")
            return
        
    else :
        os.mkdir(FolderName)
        print("Directory For Log files get created")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    print(timestamp)

    File_Name = os.path.join(FolderName , "Marvellous_%s.log"%timestamp)
    print("Log File gets created with name : ",File_Name)

    fobj = open(File_Name,"w")
    
    fobj.write(Border+"\n")
    fobj.write("----------------Marvellous Platform Surveillance System---------------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write("----------------------------End of Log File---------------------------\n")
    fobj.write(Border+"\n")

def main():
    Border = "-"*70
    print(Border)
    print("---------------Marvellous Platform Surveillance System----------------")
    print(Border)

    if(len(sys.argv) == 2):

        # py Demo.py --h or py Demo.py --H
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1. Create the automatic logs")
            print("2. Executes periodically")
            print("3. Sends mail with autolog")
            print("4. Store information about processes")
            print("5. Store information about the CPU")
            print("6. Store information about the RAM storage")
            print("7. Stores the information about the secondary storage")

        # py Demo.py --u or py Demo.py --U
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of the directory to create the auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # py Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time Interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])

        # Apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Surveillance System Started sucessfully")
        print("Directory created",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invalid number of arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("------------------Thank You For using Our Script----------------------")
    print(Border)

if __name__ == "__main__":
    main()