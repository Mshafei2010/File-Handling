## Key
- [Text File Handling in Python](#text-file-handling-in-python)
- [CSV File Handling in Python](#csv-file-handling-in-python)
- [JSON File Handling in Python](#json-file-handling-in-python)

---

# Text File Handling in Python

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
- [Code](#code)
- [Example](#example)

---

# CSV File Handling in Python

## CSV Description
This Python script allows users to read and display the contents of a CSV file. It reads the file, extracts the field names (headers), and prints the first 100 rows of the data with a row counter.

## CSV Overview
1. The script opens the CSV file located at the specified file path.
2. The script performs the following operations:
   - **Field Extraction:** Extracts the field names (headers) from the first row of the CSV file.
   - **Row Extraction:** Reads and stores each row of data from the CSV file.
   - **Data Display:** Displays the first 100 rows of the data along with the corresponding field names, with each row preceded by a counter.
3. The output is printed to the console.

## CSV Output

- **After running the script, you will see:**
    - Field names (headers) printed in a tab-separated format.
    - The first 100 rows of the CSV file printed, with each value tab-separated and prefixed by a row counter.

## CSV Code
```python
import csv

file = open("PUT YOUR FILE PATH/diabetes.csv", "r")

fields = []
rows = []

with file as csvfile:
    csvreader = csv.reader(file)

    # extracting field names through first row
    fields = next(csvreader)
    
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for label in fields:
    print(label, end="\t")
print("\n")

counter = 1
for row in rows[:100]:
    print(counter)
    for col in row:
        print("  ", col, end="\t\t")
    print("\n")
    counter += 1
```

## CSV Example 

```
Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome	

1
  6  		148  		72  		35  		0  		33.6  		0.627  		50  		1		

2
  1  		85  		66  		29  		0  		26.6  		0.351  		31  		0		

... (additional rows)

100
  2  		90  		68  		42  		0  		38.2  		0.503  		27  		0		
```

## Key
- [Description](#CSV-description)
- [Overview](#CSV-overview)
- [Output](#CSV-output)
- [Code](#CSV-code)
- [Example](#CSV-example)

---

# JSON File Handling in Python

## Json Description
This Python script demonstrates how to handle JSON data by converting between JSON and Python dictionary formats. It includes examples of loading JSON data into a Python dictionary and dumping a Python dictionary to a JSON formatted string.

## Overview
1. **Convert from JSON to Python Dictionary**:
   - The script takes a JSON formatted string and converts it into a Python dictionary using the `json.loads()` function.
   - The values of specific keys are then printed to the console.

2. **Convert from Python Dictionary to JSON**:
   - The script defines a Python dictionary and converts it to a JSON formatted string using the `json.dumps()` function.
   - The JSON data is printed with indentation for readability and keys sorted.

## Json Output

- **After running the script, you will see:**
    - The values of specific keys from the JSON data printed to the console.
    - A formatted JSON string output from the Python dictionary, with sorted keys and indentation.

## Json Code
```python
import json

"""
Convert from Json to Python Dictionary
"""

# Sample Json Data
JsonData = '{"userId": 1,"id": 1,"title": "delectus aut autem","completed": false}'

# Conversion
data = json.loads(JsonData)

# Output Data
print(data["userId"])
print(data["title"])
print(data["completed"])

print("\n----------\n")

"""
Convert from Python Dictionary to Json
"""

# Sample Dictionary Data
rawData = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Convert data to Json with 4 indent before each key also sort keys
JSON = json.dumps(rawData, indent=4, sort_keys=True)

# Output Json
print(JSON)
```

## Json Example 

```
1
delectus aut autem
False



----------
{
    "age": 30,
    "city": "New York",
    "name": "John"
}
```

## Key
- [Description](#Json-description)
- [Overview](#Json-overview)
- [Output](#Json-output)
- [Code](#Json-code)
- [Example](#Json-example)
