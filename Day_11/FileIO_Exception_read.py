
def main():
    fobj = None
    try:
        fobj = open("Hello.txt","r")
        print("File gets successfully opened...")
        Data = fobj.read()

        print("Data from file is : ",Data)

    except FileNotFoundError:
        print("Error : Unable to open file as there is no such file")
    finally : 
        print("End of application!!!")
        fobj.close()
if __name__ == "__main__":
    main()