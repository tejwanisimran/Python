import multiprocessing
import time
import os


def SumEven(No):
    print("PID of SumEven : ",os.getpid())       # 51(svatacha)
    print("PPID of SumEven : ",os.getppid())     # 21(parent i.e main)

    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum + i

    print("Even Sum is : ",Sum)

def SumOdd(No):
    print("PID of SumOdd : ",os.getpid())        # 101(svatacha)
    print("PPID of SumOdd : ",os.getppid())      # 21(parent i.e main)

    Sum = 0
    for i in range(1,No+1,2):
        Sum = Sum + i

    print("odd Sum is : ",Sum)


def main():

    print("PID of main : ",os.getpid())          # 21(svatacha)
    print("PPID of main : ",os.getppid())        # CMD 11

    start_time = time.time()

    t = multiprocessing.Process(target = SumEven , args = (100000000,))
    
    t2 = multiprocessing.Process(target = SumOdd , args = (100000000,))
    t.start()
    t2.start()

    t.join()
    t2.join()
    
    end_time = time.time()

    print("Time requried : ",end_time - start_time)

if __name__ == "__main__":
    main()