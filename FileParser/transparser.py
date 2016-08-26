#!/usr/bin/env python
import os
import re
import sets
import common

def GetLocationName():
	# Back slash hyphen in regex means a real hyphen character
	locationExpression = re.compile("([a-zA-Z ]*)[0-9\-]*.csv")
	locations = []
	# if f.endswith(".csv") and bool(re.search(r'\d', f)) 
	# used to filer filename
	files = [f for f in os.listdir('./Trans')]

	# Get all locations mentioned in middle files.
	# Can contain duplicated location.
	for f in files:
		f = "./Trans/" + f
		location = locationExpression.search(f)
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

def CompileTransFiles(location):
	# Bellevue middle files does not match format.
	# Bellevue data file is missing.
	# Summarize the pokemon species for now.
	# TODO: calculate experience and candy as well.

	# Without unicode flag, \d equals [0-9]
	files = [f for f in os.listdir('./Trans')]

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
		f = "./Trans/" + f
		size = os.path.getsize(f)
		totalSize += size

	fileSummary = ', '.join(fileList)
	print("=> Start processing %s." % fileSummary)
	print("=> Input data size is %s byte(s)." % totalSize)

def SummarizeSpecies(fileList):
	# If location kinds >= 2.
	# I want to know:
	# Total species, unique species in location, common species
	locationExpression = re.compile("([a-zA-Z ]*)[0-9\-]*.csv")
	locations = sets.Set()
	for f in fileList:
		location = locationExpression.match(f)
		if location:
			locations.add(location.group(1))

	# \s matches any space when UNICODE flag is not set
	# + matches one or more preceding charater
	rowExpression = re.compile("([A-Za-z\.\s]*)\s+[0-9].*")

	# for each location, create the set of species
	species = {}
	for location in locations:
		species[location] = sets.Set()

	for f in fileList:
		location = locationExpression.match(f)
		if location:
			loc = location.group(1)
			f = "./Trans/" + f
			with open(f, "r") as content:
				for line in content:
					match = rowExpression.match(line)
					if match:
						species[loc].add(match.group(1))

	# if there are more than one locations
	if len(species) > 1:
		total = sets.Set()
		common = sets.Set()

		# calculate union and intersect
		for key in species:
			total = total.union(species[key])
			if len(common) == 0:
				common = species[key]
			else:
				common = common.intersection(species[key])

		# calculate difference
		# defined as this kind at least not appear in one location
		# TODO: should use O(n^2) to diff every other location
		for key in species:
			species[key] = species[key].difference(common)

		species["total"] = total
		species["common"] = common

	return species

def PrintToFinalFile(species, outputFile):
	# species is a dictionalry of set
	output = open(outputFile, "w")
	for key in species:
		output.write("==== " + key.upper() + " ====" + "\n")
		if key != "total":
			for value in species[key]:
				output.write(value + "\n")
		output.write("\ntotal: %s\n\n" % len(species[key]))

	output.close()
	print("=> Output size is %s byte(s)." % os.path.getsize(outputFile))
	return
