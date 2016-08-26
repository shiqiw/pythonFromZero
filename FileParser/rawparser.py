#!/usr/bin/env python
import datetime
import os
import re
import sys
import common

def GetDataFileName():
	# listdir return a list of file names, using relative path
	# To search for certain file type:
	#files = [f for f in os.listdir('.') if f.endswith(".txt")]
	mostRecentFile = ""
	optionMarker = "A"
	defaultMarker = ""
	options = {}

	for f in os.listdir('./Raw'):
		# O(n) to get most recent modified file.
		f = './Raw/' + f
		if mostRecentFile == "":
			mostRecentFile = f
		else:
			if (os.path.getmtime(f) > os.path.getmtime(mostRecentFile)):
				mostRecentFile = f

		# Create option, set default option to most recent file
		options[optionMarker] = f
		if f == mostRecentFile:
			defaultMarker = optionMarker
		optionMarker = chr(ord(optionMarker) + 1)

	# No data file is available
	if len(options) == 0:
		return ""

	return common.QueryUserChoice("Please select raw file to process.", options, defaultMarker)

def CompileDataFile(dataFile):
	print("=> Start processing %s." % dataFile)
	print("=> Input data size is %s byte(s)." % os.path.getsize(dataFile))

	dictionary = {}
	# python regex, '.' any char, '*' zero or more preceding char
	captureExpression = re.compile("We caught a (.*) with")
	# '(','|' are special char, need escape, '+' is one or more preceding
	captureExpression1 = re.compile("\(CatchSuccess.* \| \([A-Za-z]+\) (.*) Lvl: [0-9]+")
	transferExpression = re.compile("] (.*) was transferred.")
	transferExpression1 = re.compile("\(TRANSFERED\) ([A-Za-z]+)\s+")

	with open(dataFile, "r") as content:
		for line in content:
			# search looks through full string
			capture = captureExpression.search(line)
			capture1 = captureExpression1.search(line)
			transfer = transferExpression.search(line)
			transfer1 = transferExpression1.search(line)

			# Bound, unbound methods
			# Instance, static and class methods
			if capture:
				if capture.group(1) in dictionary:
					dictionary[capture.group(1)] = dictionary[capture.group(1)].Capture()
				else:
					# If not instantiate, get unbound method Capture() must be called 
					# with PokemonRecord instance as first argument (got nothing instead)
					dictionary[capture.group(1)] = common.PokemonRecord().Capture()

			if capture1:
				if capture1.group(1) in dictionary:
					dictionary[capture1.group(1)] = dictionary[capture1.group(1)].Capture()
				else:
					dictionary[capture1.group(1)] = common.PokemonRecord().Capture()

			if transfer:
				if transfer.group(1) in dictionary:
					dictionary[transfer.group(1)] = dictionary[transfer.group(1)].Transfer()
				else:
					dictionary[transfer.group(1)] = common.PokemonRecord().Transfer()

			if transfer1:
				if transfer1.group(1) in dictionary:
					dictionary[transfer1.group(1)] = dictionary[transfer1.group(1)].Transfer()
				else:
					dictionary[transfer1.group(1)] = common.PokemonRecord().Transfer()

	return dictionary

def GetTransFileName(dataFile):
	# Define data file name starts with location info
	# Match looks in beginning of the string
	# Search looks through entire string
	locationExpression = re.compile("([a-zA-Z ]*)[0-9]*.txt")
	location = locationExpression.search(dataFile)

	# This is get current time
	#time = datetime.datetime.now().strftime("%Y-%m-%d-%H")
	# This is get data file last  modified time
	time = datetime.datetime.fromtimestamp(os.path.getmtime(dataFile))
	formatTime = time.strftime("%Y-%m-%d-%H")

	if location:
		return "./Trans/{0}-{1}.csv".format(location.group(1), formatTime)
	else:
		return "./Trans/" + formatTime + ".csv"

def PrintToTransFile(content, transFile):
	print("=> Start writing to output %s." % transFile)

	output = open(transFile, "w")
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
	print("=> Output size is %s byte(s)." % os.path.getsize(transFile))
	return