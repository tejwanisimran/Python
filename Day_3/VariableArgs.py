def Addition(*No):
    print(No)           # 11,21,51,101
    print(type(No))     # tuple
    print(len(No))      # 4


def main():
    Addition(11,21,51,101,11)
    

if __name__ == "__main__":
    main()