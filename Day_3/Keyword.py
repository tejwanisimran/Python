def EmployeeInfo(Name,Age,Salary,City):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)


def main():
    #EmployeeInfo("Rahul",26,2000.50,"Pune")     # Corect
    #EmployeeInfo(26,"Rahul","Pune",2000.5)      # Wrong

    #Keyword Arguments
    EmployeeInfo(Age = 26 , Name = "Rahul",City = "Pune",Salary = 2000.50)   # Correct


if __name__ == "__main__":
    main()