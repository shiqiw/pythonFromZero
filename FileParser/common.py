#!/usr/bin/env python
import collections
import sys

def QueryUserChoice(question, options, default):
	"""
	Prompt user a question with choices.
	question: a string like "Please select an input file."
	options: a dictionary like {"A": "Bellevue.txt"}
	default: a string like "A"
	Return user choice value.
	"""
	# TODO: Build validate dictionary according to options like 
	# {"A": "Bellevue.txt"} => {"A": "Bellevue.txt", "a": "Bellevue.txt", "Bellevue": "Bellevue.txt"}
	# Right now use options as validate dictionary
	while True:
		sys.stdout.write("=> " + question + "\n")

		# Use sorted dictionary to print ordered output.
		sortedOptions = collections.OrderedDict(sorted(options.items()))
		for key in sortedOptions:
			sys.stdout.write("   " + key + ". " + sortedOptions[key] + "\n")
			
		sys.stdout.write("   Default choice is " + default + ".\n")
		sys.stdout.write("   Please input your choice or press enter to use default: ")

		choice = raw_input().upper()
		if default is not None and choice == '':
			return options[default]
		elif choice in options:
			return options[choice]
		else:
			sys.stdout.write("Oops. Cannot quite understand. Let's try again.\n")

# import enum
# class Bot(enum.Enum):
# 	NecroBot = 1
# 	PoGoRocketApiBot = 2

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

	# TODO: introduce evolve action