# File Handling in Python

## Description
This Python script demonstrates various file handling operations including creating, writing, reading, appending, and deleting files. The operations are performed on text files, with each section of the script handling a different aspect of file management.

## Overview
1. **Create File**:
   - The script creates a new file using the `open` function with the mode `"x"`. The file is created at the specified path.

2. **Write File**:
   - The script opens a file in write mode `"w"` and writes multiple lines of text into it using the `write` and `writelines` functions.

3. **Read File**:
   - The script reads content from a file using different methods like `read`, `readlines`, and `seek`. It demonstrates how to read specific parts of a file and reset the file pointer to read the content again.

4. **Read and Write File**:
   - The script demonstrates how to open a file in read and write mode `"r+"`. It writes data to the file and then reads it back using the `readlines` function.

5. **Delete File**:
   - The script uses the `os.remove()` function to delete a specified file from the system.

6. **Append File**:
   - The script opens a file in append mode `"a+"` to add additional data to the file without overwriting the existing content. It then reads the updated content.

## Output

- **After running the script, you will see:**
    - The creation of new files at specified paths.
    - Written content output in the console after performing read operations.
    - Appended content displayed after adding new data to an existing file.
    - Confirmation that a specified file has been deleted.

## Code
```python
import os

"""
Create File
"""
# Create file
create_file = open("D:/Courses/given/nefham/projects/File Handling/createFile.txt", "x")
create_file.close()

"""
Write File
"""
# Create file
write_file = open("D:/Courses/given/nefham/projects/File Handling/writeFile.txt", "w")
Lines = ["This is Mohamed Shafei\n", "Graduated from Computer Science\n", "Python Developer\n"]

# Write in file
write_file.write("Info:\n")
write_file.writelines(Lines)

# Close file
write_file.close()

"""
Read File
"""
read_file = open("D:/Courses/given/nefham/projects/File Handling/writeFile.txt", "r")

# Read part
print(read_file.read(5))  # prints "Info:"
print(read_file.read(6))  # prints "\nThis"

# Data begins from "is"
print(read_file.readlines())

# Prints all data; not part, so we use seek
read_file.seek(0)
print(read_file.readlines())

# Close file
read_file.close()

"""
Read and Write File
"""
# Create file
read_write_file = open("D:/Courses/given/nefham/projects/File Handling/readwriteFile.txt", "w")
read_write_file.close()

# Read and write in file
read_write_file = open("D:/Courses/given/nefham/projects/File Handling/readwriteFile.txt", "r+")

# Add data
read_write_file.write("This is my info\n")
read_write_file.writelines(Lines)

# Prints nothing as new data is not sought
print(read_write_file.readlines())

# To get the new lines added
read_write_file.seek(0)

# Prints new data
print(read_write_file.readlines())

# Close file
read_write_file.close()

"""
Delete File
"""
os.remove("D:/Courses/given/nefham/projects/File Handling/createFile.txt")

"""
Append File
"""
# Create file and write data in
append_file = open("D:/Courses/given/nefham/projects/File Handling/appendFile.txt", "w")
append_file.write("This file contains data and we will append to it\n")
append_file.close()

# Append to file
append_file = open("D:/Courses/given/nefham/projects/File Handling/appendFile.txt", "a+")

# Append data
append_file.write("We appended Hello")

# Print data
append_file.seek(0)
print(append_file.readlines())

# Close file
append_file.close()
```

## Example 

```
Info:
This
[' is Mohamed Shafei\n', 'Graduated from Computer Science\n', 'Python Developer\n']
['Info:\n', 'This is Mohamed Shafei\n', 'Graduated from Computer Science\n', 'Python Developer\n']
[]
['This is my info\n', 'This is Mohamed Shafei\n', 'Graduated from Computer Science\n', 'Python Developer\n']
['This file contains data and we will append to it\n', 'We appended Hello']
```

## Key
- [Description](#description)
- [Overview](#overview)
- [Output](#output)
- [Code](#Code)
- [Example](#Example)

---

This README provides clear instructions and explanations for anyone using or reviewing the file handling script.