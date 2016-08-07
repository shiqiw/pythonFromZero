#!/usr/bin/env python
import os
import sets
import common
import csvparser
import txtparser

def main():
	# Select parser for .txt file or .csv file.
	# Define data file as .txt file and result file as .csv file.
	option = common.QueryUserChoice("Please select file type.", 
									{"A": "txt", "B": "csv"}, 
									"A")

	# Define parameter name as data and result.
	if option == "txt":
		dataFile = txtparser.GetDataFileName()
		if dataFile == "":
			print("=> No meat for grinding. Exit.")
			return
		content = txtparser.CompileDataFile(dataFile)
		resultFile = txtparser.GetResultFileName(dataFile)
		txtparser.PrintToResultFile(content, resultFile)
	# Define parameter as middle and final.
	else:
		middleFile = csvparser.GetLocationName()
		if middleFile == "":
			print("=> No meat for grinding. Exit.")
			return
		summary = csvparser.CompileMiddleFile(middleFile)
		finalFile = middleFile + ".csv"
		csvparser.PrintToFinalFile(summary, finalFile)
		
	print("=> Finish.")
	return

# This function will be 
# automatically selected as 
# the start point of execution
main()