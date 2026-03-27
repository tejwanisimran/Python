## Day 11 :

## Conceptual codes to understand File I/O in python & start of directory automation.

---

## File I/O in Python : 

- File is named location on disk to store related information.
- It is used to permanently store data in a non-volatile memory.
- Hence in Python , file operations takes place in the following order :
  ```
  1. Open a file
  2. Read or Write(perform operation).
  3. Close a file.

  ```
---
## 1. Open a file : 

- Python has a built-in open() function to open a file.
- This function returns a file object ,also called as a handle ,as it is used to read or modify the file accordingly.
- Synatx :
  ```
  fd1 = open(FileName , mode)
  where :
  mode can be read , write ,  read write in binary mode , etc.
  ```
---

## Close a file : 

- When we are done with the operations to the file , we need to properly close the file.
- Syntax :
  ```
  fd1.close()
  ```
---

## Read data from the file : 

- To read a file in python , we must open the file in reading mode.
- Synatx :
  ```
  fd1.read()
  - It would read till end of the file.
  ```
---

## Write the data into the file : 

- In order to write into a file in python , we need to open it in write mode.
- Syntax :
  ```
  fd1.write("Python : Automation & Machine Learning.")
