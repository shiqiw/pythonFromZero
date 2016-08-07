#!/usr/bin/env python
import datetime
import os
import re
import sys
import common

def GetDataFileName():
	# listdir return a list of names.
	files = [f for f in os.listdir('.') if f.endswith(".txt")]
	mostRecentFile = ""
	optionMarker = "A"
	defaultMarker = ""
	options = {}

	for f in files:
		# O(n) to get most recdnt modified file.
		if mostRecentFile == "":
			mostRecentFile = f
		else:
			if (os.path.getmtime(f) > os.path.getmtime(mostRecentFile)):
				mostRecentFile = f

		options[optionMarker] = f
		if f == mostRecentFile:
			defaultMarker = optionMarker
		optionMarker = chr(ord(optionMarker) + 1)

	if len(options) == 0:
		return ""

	return common.QueryUserChoice("Please select file name.", options, defaultMarker)

def CompileDataFile(inputFile):
	print("=> Start processing %s." % inputFile)
	print("=> Input data size is %s byte(s)." % os.path.getsize(inputFile))

	dictionary = {}
	captureExpression = re.compile("We caught a (.*) with")
	captureExpression1 = re.compile("\(CatchSuccess.* \| \([A-Za-z]+\) (.*) Lvl: [0-9]")
	transferExpression = re.compile("] (.*) was transferred.")

	with open(inputFile, "r") as content:
		for line in content:
			capture = captureExpression.search(line)
			capture1 = captureExpression1.search(line)
			transfer = transferExpression.search(line)

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

	return dictionary

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

def PrintToResultFile(content, outputFile):
	print("=> Start writing to output %s." % outputFile)

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
	print("=> Output size is %s byte(s)." % os.path.getsize(outputFile))
	return