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
    fobj.write(Border+"\n\n")
    fobj.write("---------------------------System Report------------------------------\n")
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()

    fobj.write("RAM Usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try : 
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s used"%(part.mountpoint,usage.percent))
        except :
            pass
    fobj.write("\n -----------------------Disk usage Report----------------------------\n")
    net = psutil.net_io_counters()
    fobj.write(Border+"\n")

    fobj.write("\n ----------------------Network Usage Report--------------------------\n")
    fobj.write("Sent : %2f MB\n"%(net.bytes_sent / (1024*1024)))
    fobj.write("Recv : %2f MB\n"%(net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")
    # ProcessLog
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n"%info.get("pid"))
        fobj.write("Name : %s\n"%info.get("name"))
        fobj.write("UserName : %s\n"%info.get("username"))
        fobj.write("Status : %s\n"%info.get("status"))
        fobj.write("StartTime : %s\n"%info.get("creat_time"))
        fobj.write("CPU %% : %2f\n"%info.get("cpu_percent"))
        fobj.write("Memory %% : %2f\n"%info.get("memory_percent"))
        fobj.write(Border+"\n")


    fobj.write("----------------------------End of Log File---------------------------\n")
    fobj.write(Border+"\n")

def ProcessScan():
    listprocess = list()

    # Warmup for CPU percent
    for proc in psutil.process_iter():
        try :
            proc.cpu_percent()
        except :
            pass
    time.sleep(0.2)

    for proc in psutil.process_iter():
        try : 
            info = proc.as_dict(attrs=("pid","name","username","status","create_time"))
            # Convert create_time
            try : 
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            listprocess.append(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

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