#!/usr/bin/env python
import os
import re
import sets
import common

def GetLocationName():
	# Back slash hyphen in regex means a real hyphen character
	locationExpression = re.compile("([a-zA-Z ]*)[0-9\-]*.csv")
	locations = []
	files = [f for f in os.listdir('.') if f.endswith(".csv") and bool(re.search(r'\d', f))]

	# Get all locations mentioned in middle files.
	# Can contain duplicated location.
	for f in files:
		location = locationExpression.match(f)
		if location:
			locations.append(location.group(1))

	optionMarker = "A"
	options = {}

	for location in locations:
		if not location in options.values():
			options[optionMarker] = location
			optionMarker = chr(ord(optionMarker) + 1)

	if len(options) == 0:
		return ""
	# Default option is to process all existing middle files.
	options[optionMarker] = "All"

	return common.QueryUserChoice("Please select location.", options, optionMarker)

def CompileMiddleFile(location):
	# Bellevue middle files does not match format.
	# Bellevue data file is missing.
	# Summarize the pokemon species for now.
	# TODO: calculate experience and candy as well.

	# Without unicode flag, \d equals [0-9]
	files = [f for f in os.listdir('.') if f.endswith(".csv") and bool(re.search(r'\d', f))]

	if location != "All":
		# Find files with a certain location.
		nameString = location + "[0-9\-]*.csv"
		nameExpression = re.compile(nameString)
		files = [f for f in files if nameExpression.match(f)]

	SummarizeTotalFileSize(files)
	return SummarizeSpecies(files)

def SummarizeTotalFileSize(fileList):
	totalSize = 0

	for f in fileList:
		size = os.path.getsize(f)
		totalSize += size

	fileSummary = ', '.join(fileList)
	print("=> Start processing %s." % fileSummary)
	print("=> Input data size is %s byte(s)." % totalSize)

def SummarizeSpecies(fileList):
	species = sets.Set()
	# \s matches any space when UNICODE flag is not set
	# + matches one or more preceding charater
	rowExpression = re.compile("([A-Za-z]*)\s+[0-9].*")

	for f in fileList:
		with open(f, "r") as content:
			for line in content:
				match = rowExpression.match(line)
				if match:
					species.add(match.group(1))

	return species

def PrintToFinalFile(species, outputFile):
	output = open(outputFile, "w")
	for s in species:
		output.write(s + "\n")	
	output.write("\n\nTotal: %s" % len(species))

	output.close()
	print("=> Output size is %s byte(s)." % os.path.getsize(outputFile))
	return
