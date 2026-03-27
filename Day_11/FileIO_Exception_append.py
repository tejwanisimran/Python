
def main():
    fobj = None
    try:
        fobj = open("Hello.txt","a")
        print("File gets successfully opened...")

        fobj.write("Python Automation")

    except FileNotFoundError:
        print("Error : Unable to open file as there is no such file")
    finally : 
        print("End of application!!!")
        fobj.close()
if __name__ == "__main__":
    main()