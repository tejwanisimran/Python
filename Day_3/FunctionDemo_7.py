# Accept : Multiple parameter
# Return :1 value

def Marvellous1(Value1,Value2):                   # Positional Arguments
    print("Inside Marvellous1 :",Value1,Value2)
    return 11

def main():
    result = None
    result = Marvellous1("Python",21)

    print("Return value is :",result)

if __name__ == "__main__":
    main()
    