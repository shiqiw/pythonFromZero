# simple file operations

# When you run a python program, its current working directory is initialized to whatever your current working directory was when you ran the program.
import os
dir = os.getcwd()
print ('current working directory is %s' % dir)

# access mode are r = read, w = write, a = append to exist file, b = open a binary file
# relative directory is from current working directory
file = open('README', 'a')
file.write('Practice file read and write.')
file.close()

# csv file contains data separated by a character, usually comma (,)

