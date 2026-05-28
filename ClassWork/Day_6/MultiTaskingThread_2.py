import threading

def Display():
    print("Inside Display Function : ",threading.get_ident())

def main():
    print("Inside Main : ",threading.get_ident())
    t1 = threading.Thread(target = Display)
    t1.start()
    print("End of main")

if __name__ == "__main__":
    main()