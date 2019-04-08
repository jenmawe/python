#This python file was written by J. Eustis 2019-04-08
#It takes an ARC report from Aleph and creates 2 text files.
#The first file created contains the bib system numbers, and
#the second holdings records numbers.
#If there is no holdings record, the entry is 0 and nothing is written to the
#text file. This does create a new line after the last item written to the file.

import csv

#Modified system numbers are stored in a list
bibSysNo = []
holSysNo = []

with open('test.csv') as csvFile:
    csvreader = csv.reader(csvFile, delimiter= ',')
    next(csvreader)
    for row in csvreader:
        if len(row[0]) == 7:
            bibSys = "00" + row[0] + "FCL01"
            bibSysNo.append(bibSys)
        elif len(row[0]) == 8:
            bibSys = "0" + row[0] + "FCL01"
            bibSysNo.append(bibSys)
        else:
            bibSys = row[0] + "FCL01"
            bibSysNo.append(bibSys)

        if len(row[9]) == 7:
            holSys = "00" + row[9] + "FCL60"
            holSysNo.append(holSys)
        elif len(row[9]) == 8:
            holSys = "0" + row[9] + "FCL60"
            holSysNo.append(holSys)
        elif row[9] == '0':
            continue
        else:
            holSys = row[9] + "FCL60"
            holSysNo.append(holSys)

#items in both lists are written to text files
with open('bibsys.txt', 'w') as txt:
    for item in bibSysNo:
        txt.write("{}\n".format(item))

with open('holsys.txt', 'w') as tfile:
    for i in holSysNo:
        tfile.write("{}\n".format(i))

csvFile.close()
txt.close()
tfile.close()
