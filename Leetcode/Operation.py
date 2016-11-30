import json
from pymongo import MongoClient
import random
import sets
import Util

class Operation(object):

	@staticmethod
	def create(collection):
		# TODO: real mode
		entry = {}

		entry["_id"] = raw_input("=> Question ID: ")
		entry["title"] = raw_input("=> Question title: ")

		try:
			entry["description"] = Util.scrape_content(entry["title"], \
				"meta", {"name": "description"}, Util.Column.DESCRIPTION)
			entry["tags"] = Util.scrape_content(entry["title"], "span", \
				{"class": "hidebutton"}, Util.Column.TAGS)
			entry["similar"] = Util.scrape_content(entry["title"], "span", \
				{"class": "hidebutton"}, Util.Column.SIMILAR)
		except:
			Util.Printer.print_warning("Unable to scrape content online.")
			entry["description"] = Util.query_paragraph( \
				"Question description:")
			entry["tags"] = Util.query_array( \
				"Question tags:")
			entry["similar"] = Util.query_array( \
				"Similar question titles:")

		entry["solutions"] = Util.query_array("Solutions:", True)

		try:
			post_id = collection.insert_one(entry).inserted_id
			Util.Printer.print_ok( \
				"Add a new entry {}, total count {}".format(post_id, collection.count()))
		except:
			# duplicate key _id insertion will throw error
			# TODO: ask whether need to update or not
			Util.Printer.print_warning("Entry already exist, update entry")
			Operation.update(collection, entry)

	@staticmethod
	def find(collection):
		# TODO: real mode
		direction = "Random"
		while True:
			direction = Util.query_option("Search direction?", \
				["Summary", "Tags", "Key word", "ID", "Random", "Exit"], direction)
			if direction == "Summary":
				print("Total entries %s" %(collection.count()))
				tags = ", ".join(collection.distinct("tags"))
				print("Tags:\n" + tags)
			elif direction == "Tags":
				tag = raw_input("=> Tag:")
				entries = collection.find({"tags": tag})
				for entry in entries:
					Util.Printer.print_entry(entry)
					if Util.query_option("Continue?", ["Yes", "No"], "Yes") == "No":
						break
			elif direction == "Key word":
				key = raw_input("=> Key word:")
				entries = collection.find({"title": {"$regex": ".*"+key+".*"}})
				# TODO: find in description as well
				# TODO: convert cursor to list or set
				# TODO: union two sets to get result
				for entry in entries:
					if Util.query_option("Continue?", ["Yes", "No"], "Yes") == "No":
						break
					Util.Printer.print_entry(entry)
			elif direction != "Exit":
				entry = {}
				if direction == "ID":
					_id = raw_input("=> Id:")
					entry = collection.find_one({"_id": _id})
				else:
					random.seed()
					rand = random.randint(0, collection.count())
					entry = collection.find().limit(-1).skip(rand).next()
				Util.Printer.print_entry(entry)

				curr = sets.Set(entry["similar"])
				next = sets.Set()
				visited = sets.Set()
				while len(curr) != 0:
					for s in curr:
						if not s in visited:
							visited.add(s)
							e = collection.find_one({"title": s})
							if e != None:
								for ns in e["similar"]:
									next.add(ns)
					curr = next
					next = sets.Set()

				print("Total similar %s" % len(visited))
				for s in visited:
					if Util.query_option("Continue?", ["Yes", "No"], "Yes") == "No":
						break
					# case sensitive problem
					e = collection.find_one({"title": s})
					if e != None:
						Util.Printer.print_entry(e)
			else:
				break

	@staticmethod
	def update(collection, entry = None):
		# TODO: real mode
		# TODO: update _id, title, description, tags and similar
		if entry == None:
			_id = raw_input("=> Question ID:")
			entry = collection.find_one({"_id": _id})

			# entry retrieved from DB can be used as dictionary
			Util.Printer.print_entry(entry)
			solutions = Util.query_array("Update solution", True, entry["solutions"])
			# when to use find_one_and_update
			collection.update_one({"_id": _id}, \
				{"$set": {"solutions": solutions}})
		else:
			# $inc can only be used with numeric value
			_id = entry["_id"]
			old_entry = collection.find_one({"_id": _id})
			solutions = old_entry["solutions"] + entry["solutions"]
			collection.update_one({"_id": _id}, \
				{"$set": {"solutions": solutions}})

	@staticmethod
	def delete(collection):
		# TODO: soft delete (enable restore) and hard delete
		_id = raw_input("=> Question ID:")

		entry = collection.find_one({"_id": _id})
		Util.Printer.print_entry(entry)

		if Util.query_option("Delete?", ["Yes", "No"], "Yes") == "Yes":
			collection.delete_one({"_id": _id})

def main():
	client = MongoClient("mongodb://localhost:27017/")
	db = client["interview"]

	name = Util.query_option("Select mode.", ["Practice", "Real"], "Practice")
	collection = db[name]
	operation = "Add"

	while True:
		# Shortly remember last operation
		operation = Util.query_option("Select operation.", ["Change mode", \
			"Add", "Find", "Update", "Delete", "Exit"], operation)
		if operation == "Change mode":
			name = Util.query_option("Select mode.", ["Practice", "Real"], "Practice")
			collection = db[name]
		elif operation == "Add":
			Operation.create(collection)
		elif operation == "Find":
			Operation.find(collection)
		elif operation == "Update":
			Operation.update(collection)
		elif operation == "Delete":
			Operation.delete(collection)
		else:
			print "Have a nice day!"
			break
main()