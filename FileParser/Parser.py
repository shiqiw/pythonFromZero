#!/usr/bin/env python
import datetime
import os
import re
import sys

def GetDataFileName():
	name = ""

	try:
		name = str(input("==> Input the file you want to parse:"))
	except:
		error = sys.exc_info()[0]
		#print(error)
		print("==> Skip to grind the most recent file.")

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

	print("==> Selected file is %s size %s byte(s)." % (name, os.path.getsize(name)))
	return name

def DefineFileNameAccordingToDateTime():
	time = datetime.datetime.now().strftime("%Y-%m-%d-%H")

	return time + ".csv"

def CompileInputFile(inputFile):
	print("==> Start processing.")

	dictionary = {}
	catchExpression = re.compile("We caught a (.*) with")
	transferExpression = re.compile("] (.*) was transferred.")

	with open(inputFile, "r") as content:
		for line in content:
			catch = catchExpression.search(line)
			transfer = transferExpression.search(line)

			if catch:
				if catch.group(1) in dictionary:
					dictionary[catch.group(1)] += 1
				else:
					dictionary[catch.group(1)] = 1

			if transfer:
				if transfer.group(1) in dictionary:
					dictionary[transfer.group(1)] -= 1
				else:
					dictionary[transfer.group(1)] = -1

	return dictionary

def PrintOutput(content, outputFile):
	print("==> Start writing to output.")

	output = open(outputFile, "w")
	total = 0

	output.write("{0:<15} {1:>3}\n".format("Name", "Count"))

	for key in content:
		total += content[key]
		output.write("{0:<15} {1:>3}\n".format(key, str(content[key])))

	output.write("\n\nTotal kinds: %s \n" % len(content.keys()))
	output.write("Total count: %s" % total)

	output.close()
	print("==> Output size %s byte(s)." % os.path.getsize(outputFile))
	return

def main():
	# Get input file
	inputFile = GetDataFileName()
	if inputFile == "":
		inputFile = GetLatestModifiedDataFileInCurrentDirectory()
	if inputFile == "":
		return

	# Based on input file name, decide parser mode

 	# Based on parser mode, decide output file name
	outputFile = DefineFileNameAccordingToDateTime()

	compileContent = CompileInputFile(inputFile)	

	PrintOutput(compileContent, outputFile)

	print("==> Finish.")
	return

main()