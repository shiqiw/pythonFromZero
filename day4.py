# simple file operations

# When you run a python program, its current working directory is initialized to whatever your current working directory was when you ran the program.
# relative directory is from current working directory
import os
dir = os.getcwd()
print ('current working directory is %s' % dir)

# access mode are r = read, w = write, a = append to exist file, b = open a binary file
# open(filename, mode = '')
# file.read() read file as a whole, and there is file.readline()
# for line in file.readlines() or xreadlines()
file = open('README', 'a')
file.write('Practice file read and write.')
file.close()

# csv file contains data separated by a character, usually comma (,)
import csv
# cvs.reader(filename, dilimeter = ',')
data = csv.reader('samplecsv.csv')
print(data)

# better solution is with ... as to ensure the clean up even program crash
filename = 'samplecsv.csv'
accessmode = 'r'
with open(filename, accessmode) as mycsv:
    data = csv.reader(mycsv)
    for row in data:
	print(row)
	for value in row:
	    print(value + '\n')
	print(','.join(row))
