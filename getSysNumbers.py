#This python file was written by J. Eustis 2019-09
#It formats system numbers for Aleph and writes them to a text file.
#The first file created contains the bib system numbers, and
#the second holdings records numbers.
#If there is no holdings record, the entry is 0 and nothing is written to the
#text file. This does create a new line after the last item written to the file.

import csv

#Modified system numbers are stored in a list that are later written to a text file
SysNo = []

#tests to ensure that answer is b or h to continue
while True:
    try:
        numberType = input("Enter B for bib sys and H for holdings: ")
        testsys = numberType.lower()
        if testsys == "b" or testsys == "h":
            break
    except:
        continue
	
#asks for csv file
sysFile = input("Please provide the CSV file name:  ")

#asks for name of txt file to write
outFile = input("Provide the output file name with .txt extension:  ")

#assigns suffix
if testsys == "b":
    suffix = "FCL01"
else:
    suffix = "FCL60"

#opens csv and formats numbers
with open(sysFile) as csvFile:
    csvreader = csv.reader(csvFile, delimiter= ',')
    for row in csvreader:
        max = len(row[0])
        missing = 9 - max
        add = "0" * missing
        systemNumber = add + row[0] + suffix
        SysNo.append(systemNumber)

#writes SysNo items to text file and ensures there is no extra line  
with open(outFile, 'w') as txt:
    for item in SysNo:
        if item == SysNo[-1]:
            txt.write("{}".format(item))
        else:
            txt.write("{}\n".format(item))

csvFile.close()
txt.close()
