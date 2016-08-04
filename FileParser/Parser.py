#!/usr/bin/env python
import datetime
import os
import re
import sys

class PokemonRecord(object):
	def __init__(self):
		self.count = 0
		self.experience = 0
		self.candy = 0

	# If not take self as parameter, get Capture() takes no arguments (1 given)
	def Capture(self):
		self.count += 1
		self.experience += 100
		self.candy += 3
		# If not return, get 'NoneType' object has no attribute 'count'
		return self

	def Transfer(self):
		self.count -= 1
		self.candy += 1
		return self

def GetDataFileName():
	name = ""

	try:
		name = str(input("==> Input the file you want to parse:"))
	except:
		error = sys.exc_info()[0]
		print("==> Skip to grind the most recent file.")
		name = GetLatestModifiedDataFileInCurrentDirectory()

	return name

def GetLatestModifiedDataFileInCurrentDirectory():
	name = ""

	# listdir return a list of names
	files = [f for f in os.listdir('.') if f.endswith(".txt")]

	for f in files:
		if name == "":
			name = f
		else:
			if (os.path.getmtime(f) > os.path.getmtime(name)):
				name = f

	return name

def GetResultFileName(inputFile):
	# Define data file name starts with location info
	# Match looks in beginning of the string
	# Search looks through entire string
	locationExpression = re.compile("([a-zA-Z ]*)[0-9]*.txt")
	location = locationExpression.match(inputFile)

	# This is get current time
	#time = datetime.datetime.now().strftime("%Y-%m-%d-%H")
	# This is get data file last  modified time
	time = datetime.datetime.fromtimestamp(os.path.getmtime(inputFile))
	formatTime = time.strftime("%Y-%m-%d-%H")

	if location:
		return "{0}-{1}.csv".format(location.group(1), formatTime)
	else:
		return formatTime + ".csv"

def CompileInputFile(inputFile):
	print("==> Start processing.")

	dictionary = {}
	captureExpression = re.compile("We caught a (.*) with")
	transferExpression = re.compile("] (.*) was transferred.")

	with open(inputFile, "r") as content:
		for line in content:
			capture = captureExpression.search(line)
			transfer = transferExpression.search(line)

			# Bound, unbound methods
			# Instance, static and class methods
			if capture:
				if capture.group(1) in dictionary:
					dictionary[capture.group(1)] = dictionary[capture.group(1)].Capture()
				else:
					# If not instantiate, get unbound method Capture() must be called 
					# with PokemonRecord instance as first argument (got nothing instead)
					dictionary[capture.group(1)] = PokemonRecord().Capture()

			if transfer:
				if transfer.group(1) in dictionary:
					dictionary[transfer.group(1)] = dictionary[transfer.group(1)].Transfer()
				else:
					dictionary[transfer.group(1)] = PokemonRecord().Transfer()

	return dictionary

def PrintOutput(content, outputFile):
	print("==> Start writing to output.")

	output = open(outputFile, "w")
	totalCount = 0
	totalExperience = 0

	output.write("{0:<15} {1:>5} {2:>5} {3:>5}\n".format("Name", "Count", "Exp", "Candy"))

	for key in content:
		record = content[key]
		totalCount += record.count
		totalExperience += record.experience
		output.write("{0:<12} {1:>5} {2:>5} {3:>5}\n".format(key, 
															record.count, 
															record.experience, 
															record.candy))

	output.write("\n\nTotal kinds: %s \n" % len(content.keys()))
	output.write("Total count: %s \n" % totalCount)
	output.write("Total Exp  : %s " % totalExperience)

	output.close()
	print("==> Output file %s size %s byte(s)." % (outputFile, os.path.getsize(outputFile)))
	return

def main():
	# Get input file. 
	# Define data file as .txt file and output file as .csv file.
	inputFile = GetDataFileName()
	if inputFile == "":
		print("==> No meat for grinding. Exit.")
		return
	else:
		print("==> Selected file is %s size %s byte(s)." % (inputFile, 
															os.path.getsize(inputFile)))

 	# Based on input file name, get output file name
	outputFile = GetResultFileName(inputFile)

	# Digest input file
	compileContent = CompileInputFile(inputFile)	

	# Print to output file
	PrintOutput(compileContent, outputFile)

	print("==> Finish.")
	return

main()