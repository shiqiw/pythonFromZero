from operation import Operation
from pymongo import MongoClient
from util import Printer, Query

def main():
	"""
	Top level script.
	"""
	# connect to database
	client = MongoClient("mongodb://localhost:27017/")
	db = client["interview"]

	# shoutly remember last mode
	name = "Backup"
	name = Query.query_option("Select mode.", ["Practice", "Backup"], name)
	collection = db[name]

	# Shortly remember last operation
	operation = "Add"

	while True:
		operation = Query.query_option("Select operation.", ["Select mode", \
			"Add", "Find", "Update", "Delete", "Exit"], operation)

		if operation == "Select mode":
			name = Query.query_option("Select mode.", ["Practice", "Backup"], name)
			collection = db[name]
		elif operation == "Add":
			Operation.add(collection)
		elif operation == "Find":
			Operation.find(collection)
		elif operation == "Update":
			Operation.update(collection)
		elif operation == "Delete":
			Operation.delete(collection)
		else:
			Printer.print_bold("Have a nice day!")
			break

if __name__ == "__main__":
	main()