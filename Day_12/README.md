## Day 12 : 

## Conceptual codes to understand directory automation.
---
## Learnt concepts like : 
---
## 1. Directory Traversal (os module)
 - Used os.walk() to iterate through directories and subdirectories.
 - This helped in accessing all files inside a folder structure efficiently.
---
## 2. Path Handling (os.path)
- Learned how to handle file paths using functions like os.path.join(), os.path.exists(), and os.path.isdir()
   to make code platform-independent and avoid path errors.
---
## 3. Hashing (MD5 - hashlib)
- Understood how to generate a checksum using MD5 hashing.
- This helps in identifying file content uniquely and is useful for detecting duplicates.
---

## 4. Duplicate File Detection
- Learned how to compare files based on their checksum values instead of file names.
- This ensures accurate detection of duplicate files even if names are different.
---
## 5. File Deletion Automation
- Implemented logic to automatically delete duplicate or unnecessary files using os.remove(), making file management efficient.
---
## 6. Empty File Detection
- Learned how to check file size using os.path.getsize() and identify empty files (0 bytes), which can then be removed.
---
