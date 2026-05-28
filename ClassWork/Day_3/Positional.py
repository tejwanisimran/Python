def Display(A,B,C,D):
    print(A,B,C,D)

def main():
    # Display(11,21)           Not Allowed -- less arguments
    # Display(10,20,30,40,50)  Not Allowed -- extra arguments
    Display(11,21,51,101)      # Allowed 

if __name__ == "__main__":
    main()