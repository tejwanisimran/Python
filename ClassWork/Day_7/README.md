# Day 7 : 
  # Conceptual codes on MultiProcessing , Thread Syncronization & Exception Handling in Python.  

# MultiProcessing in Python :   

- Multiprocessing in Python is a technique that allows a program to run multiple processes simultaneously,
   using multiple CPU cores to achieve true parallel execution.
- # multiprocessing.Pool :
- Pool allows you to manage a pool of the worker processes to run task in parallel.It automatically handles
   process creation & load distribution.  
- Syntax :

           import multiprocessing

           p1 = multiprocessing.Process(target = FunctionName , args = (number , ))

- where number = number of process you want to create.

# Thread Syncronization in Python : 

- Thread synchronization in Python is a technique used to control the execution of multiple threads so that they
  can safely access shared resources (like variables, files, or data structures) without causing errors or inconsistencies.
  
  # Why Synchronization is Needed  

- When multiple threads run at the same time and try to modify shared data, it can lead to a race condition.  

👉 Race Condition = When output depends on the order of thread execution (unpredictable results)   

# 🔹 How Synchronization is Achieved  

- Python provides synchronization tools in the threading module.  
  1. Lock : Ensures only one thread at a time accesses shared resource  

# Exception Handling in Python :

- An exception is an unwanted or an unexpected event, which occurs during the execution of a program i.e
  at run time that disrupts the normal flow of the program instruction.
- To handle tese exception we use Exception Handling.
- For Exception Handling in Python we use 3 keywods as :
  # 1. try :
- The code which is written inside the try block is considered as an exception prone code means may generate an exception.
  # 2. except :
- This block is called as exception handler which gets executed when exception is occured.
  # 3. finally :
- This block is executed always irrespective of the exception .Generally this  lock is used to release all the resources.    
