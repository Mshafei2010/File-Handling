# File Handling

import os

"""
Create File
"""
#Create file
create_file = open("PUT YOUR FILE PATH/createFile.txt", "x")

create_file.close()

"""
Write File
"""

#Create file
write_file = open("PUT YOUR FILE PATH/writeFile.txt", "w")
Lines = ["This is Mohamed Shafei\n" , "Graduated from Computer Science\n" ,"Python Developer\n" ]

#Write in file
write_file.write("Info:\n")
write_file.writelines(Lines)

#close file
write_file.close()

"""
Read File
"""

read_file = open("PUT YOUR FILE PATH/writeFile.txt", "r")

#read part
print(read_file.read(5)) # print (Info:) 
print(read_file.read(6)) # print: newline -> This

#data begin from is
print(read_file.readlines())

# prints all data not part we use seek
read_file.seek(0)
print(read_file.readlines())


"""
Read and Write File
"""
#Create File
read_write_file = open("PUT YOUR FILE PATH/readwriteFile.txt", "w")
read_write_file.close()

#Read and write in file
read_write_file = open("PUT YOUR FILE PATH/readwriteFile.txt", "r+")

#add Data
read_write_file.write("This is my info\n")
read_write_file.writelines(Lines)

# prints nothing new data is not sought
print(read_write_file.readlines())

# to get the new lines added
read_write_file.seek(0)

# prints new data
print(read_write_file.readlines())


# close file
read_write_file.close()


"""
Delete File
"""

os.remove("PUT YOUR FILE PATH/createFile.txt")

"""
append file
"""
# Create file and write data in
append_file=open("PUT YOUR FILE PATH/appendFile.txt","w")
append_file.write("this file contain data and we will append on it\n")
append_file.close()


# Append on file
append_file=open("PUT YOUR FILE PATH/appendFile.txt","a+")

# Append Data 
append_file.write("We appended Hello")

# print data
append_file.seek(0)
print(append_file.readlines())

# Close file
append_file.close()