# In this program we have read the data from the file but only first 6 bytes.
def main():
    fobj = None
    try:
        fobj = open("Hello.txt","r")
        print("File gets successfully opened...")
        Data = fobj.read(6)

        print("Data from file is : ",Data)

    except FileNotFoundError:
        print("Error : Unable to open file as there is no such file")
    finally : 
        print("End of application!!!")
        fobj.close()
if __name__ == "__main__":
    main()