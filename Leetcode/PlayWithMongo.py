"""
Usage info:
Enter program by 'python PlayWithMongo.py'
Exit program by 'exit'
Create entry by 'add', then prompt for each column value
- If entry already exist, confirm for update existing entry
Read entry by 'find', then prompt for search query
- Give option to print to console or output to file in certain format
Update entry by 'set <ID>', then prompt for each field 
Delete entry by 'del <ID>', then print info to console, confirm deletion
"""

# Function names should be lowercase, 
# with words separated by underscores as necessary to improve readability.
# Always use self for the first argument to instance methods.
# Always use cls for the first argument to class methods.
# Use one leading underscore only for non-public methods and instance variables.
# Constants are usually defined on a module level 
# and written in all capital letters with underscores separating words. 

import datetime
# https://api.mongodb.com/python/current/tutorial.html
from pymongo import MongoClient
from Utility import Operation

# relational database is more useful for this purpose
# but can achieve with indexing and query
# table format: _id, title, content, tag, company, thought, passRecord

#def initialize():
	# the following is using default host and port
	# client = MongoClient()
	# can define own port, but ./mongod by default use 27017
	# to change, use --port <port number>
	#client = MongoClient('mongodb://localhost:27017/')

	# you can use any name for database and collection, 
	# mongo will create the db and collection for you if not already there.
	#db = client['interview']

	#return client

def main():
	client = MongoClient('mongodb://localhost:27017/')
	db = client['interview']

	while True:
		userInput = raw_input("Choose your operation: a)dd, f)ind, s)et, d)el and e)xit. \n>>")
		value = Operation.decide_operation(userInput)

		if value == Operation.CREATE:
			Operation.create_operation(db.posts)
			pass
		elif value == Operation.READ:
			print "Going to fetch data"
			pass
		elif value == Operation.UPDATE:
			print "Going to update data"
			pass
		elif value == Operation.DELETE:
			print "Going to delete data"
			pass
		elif value == Operation.EXIT:
			client.close()
			print "Have a nice day!"
			break
		else:
			print "Input is not valid."
			pass

main()