#!/usr/bin/env python
import common
import rawparser
import transparser

def main():
	# Select parser.
	# Define data file as raw file and trans-product as trans file.
	option = common.QueryUserChoice("Please select file type.", 
									{"A": "raw", "B": "trans"}, 
									"A")

	# Define parameter name as data and result.
	if option == "raw":
		dataFile = rawparser.GetDataFileName()
		if dataFile == "":
			print("=> No meat for grinding. Exit.")
			return
		content = rawparser.CompileDataFile(dataFile)
		transFile = rawparser.GetTransFileName(dataFile)
		rawparser.PrintToTransFile(content, transFile)
	# Define parameter as middle and final.
	else:
		location = transparser.GetLocationName()
		if location == "":
			print("=> No meat for grinding. Exit.")
			return
		summary = transparser.CompileTransFiles(location)
		finalFile = "./Final" + location + ".csv"
		transparser.PrintToFinalFile(summary, finalFile)
		
	print("=> Finish.")
	return

# This function will be 
# automatically selected as 
# the start point of execution
main()