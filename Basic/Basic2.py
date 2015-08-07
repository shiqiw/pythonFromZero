# Python list
guest = ['one', 'two', 'three']
# Last entry
print(guest[-1])

guest.append('four')
# Second last entry
print(guest[-2])
# similarly there is remove
# or del list[n]

# list.index(entry value) return index
# if does not exist, code crash

#len(list) built-in
#list.sort() built-in

for g in guest:
    print(g)





# File operation

# When you run a python program, its current working directory is initialized to whatever 
# your current working directory was when you ran the program.
# Relative directory is from current working directory
# cwd = current working directory
import os
dir = os.getcwd()
print ('current working directory is %s' % dir)

# Access mode are r = read, w = write, a = append to exist file, b = open a binary file
# open(filename, mode = '')
# file.read() read file as a whole, and there is file.readline()
# for line in file.readlines() or xreadlines()
file = open('README', 'a')
file.write('Practice file read and write.')
file.close()

# Csv file contains data separated by a character, usually comma (,)
import csv
# cvs.reader(filename, dilimeter = ',')
data = csv.reader('samplecsv.csv')
print(data)

# Better solution is 'with ... as' to ensure the clean up even program crash
filename = 'samplecsv.csv'
accessmode = 'r'
with open(filename, accessmode) as mycsv:
    data = csv.reader(mycsv)
    for row in data:
		print(row)
		for value in row:
		    print(value + '\n')
		# split() built-in, by defualt split on space
		print(','.join(row))





# Python function
def printHello(msg):
    print('hello ' + msg)
    return

# similarly, params are separated by comma
printHello('world')

# import other files
import Basic2Helper

def main():
    secret = Basic2Helper.getName()
    Basic2Helper.printName(secret)
    return

main()
