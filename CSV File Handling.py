# CSV File Handling

import csv

file= open("PUT YOUR FILE PATH/diabetes.csv","r")

fields= []
rows=[]

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
        print("  ",col,end="\t\t")
    print("\n")
    counter+=1