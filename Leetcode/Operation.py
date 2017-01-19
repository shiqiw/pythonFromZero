from datetime import date
from pymongo import MongoClient
import random
import sets
import sys
from util import Printer, Query, Scraper

class Operation(object):

	@staticmethod
	def add(collection):
		entry = {}

		entry["_id"] = Query.query_line("Question ID: ")
		entry["title"] = Query.query_line("Question title: ")
		entry["company"] = Query.query_array("Question company: ")

		try:
			entry["description"] = Scraper.scrape_content(entry["title"], \
				"meta", {"name": "description"}, Scraper.DESCRIPTION)
		except: #TypeError as e:
			#print sys.exc_info()[0]
			Printer.print_warning("Unable to scrape description.")
			entry["description"] = Query.query_paragraph( \
				"Question description:")

		try:
			entry["tags"] = Scraper.scrape_content(entry["title"], "span", \
				{"class": "hidebutton"}, Scraper.TAGS)
			entry["similar"] = Scraper.scrape_content(entry["title"], "span", \
				{"class": "hidebutton"}, Scraper.SIMILAR)
		except:
			Printer.print_warning("Unable to scrape tags or similar.")
			entry["tags"] = Query.query_array( \
				"Question tags: ")
			entry["similar"] = Query.query_array( \
				"Similar question titles: ")

		entry["solutions"] = Query.query_array("Solutions: ", True)

		try:
			post_id = collection.insert_one(entry).inserted_id
			Printer.print_ok( \
				"Add a new entry {}, total count {}".format(post_id, collection.count()))
		except:
			# duplicate key _id insertion will throw error
			# TODO: ask whether need to update or not
			Printer.print_warning("Entry already exist, update entry.")
			Operation.update(collection, entry)

	@staticmethod
	def find(collection):
		direction = "Random"
		while True:
			direction = Query.query_option("Search direction?", \
				["Summary", "Company", "Tags", "Key word", "ID", \
				"Random", "All", "Exit"], direction)

			if direction == "Summary":
				Operation.summary(collection)

			elif direction == "Key word":
				Operation.key(collection)

			elif direction == "Company":
				Operation.company(collection)

			elif direction == "Tags":
				Operation.tags(collection)

			elif direction == "All":
				Operation.all(collection)

			elif direction != "Exit": # ID or Similar
				entry = {}
				if direction == "ID":
					_id = raw_input("=> Id:")
					entry = collection.find_one({"_id": _id})
				else:
					random.seed()
					rand = random.randint(0, collection.count())
					# TODO: check null 
					entry = collection.find().limit(-1).skip(rand).next()
				Operation.expand(collection, entry)

			else:
				break

	@staticmethod
	def summary(collection):
		ids = collection.count()
		tags = collection.distinct("tags")

		Printer.print_bold( \
			"Progress: count ({}/455), tags ({}/31)".format(ids, len(tags)))
		Printer.print_normal(", ".join(tags))

	@staticmethod
	def key(collection):
		# TODO: find in description and tags as well
		k = Query.query_line("Key word:")
		entries = collection.find({"title": {"$regex": ".*"+k+".*"}})
		Printer.print_multi_entry_console(entries)

	@staticmethod
	def company(collection):
		c = Query.query_line("Company:")
		entries = collection.find({"company": c})
		Printer.print_multi_entry_console(entries)

	@staticmethod
	def tags(collection):
		tag = Query.query_line("Tag:")
		entries = collection.find({"tags": tag})
		Printer.print_multi_entry_console(entries)

	@staticmethod
	def all(collection):
		# TODO: find in description and tags as well
		entries = collection.find()
		Printer.print_multi_entry_console(entries)

	@staticmethod
	def expand(collection, entry):
		# TODO: memory management
		if entry == None:
			return
		entries = []
		entries.append(entry)

		curr = sets.Set(entry["similar"])
		next = sets.Set()
		useful = sets.Set()
		discard = sets.Set([entry["title"]])
		while len(curr) != 0:
			for s in curr:
				if not (s in useful or s in discard):
					e = collection.find_one({"title": s})
					if e != None:
						useful.add(s)
						entries.append(e)
						for ns in e["similar"]:
							next.add(ns)
					else:
						discard.add(s)
			curr = next
			next = sets.Set()

		print("Total similar %s" % len(useful))
		Printer.print_multi_entry_console(entries)

	@staticmethod
	def update(collection, entry = None):
		# TODO: update _id, title, description
		# TODO: when to use find_one_and_update
		if entry == None:
			_id = Query.query_line("Question ID:")
			entry = collection.find_one({"_id": _id})

		# entry retrieved from DB can be used as dictionary
		Printer.print_entry_file(entry)

		if Query.query_option("Update description?", ["Yes", "No"], "Yes") == "Yes":
			description = Query.query_paragraph("Update description.")
			collection.update_one({"_id": _id}, \
				{"$set": {"description": description}})

		if Query.query_option("Update company?", ["Yes", "No"], "Yes") == "Yes":
			company = Query.query_array("Update company.")
			collection.update_one({"_id": _id}, \
				{"$set": {"company": company}})

		if Query.query_option("Update tags?", ["Yes", "No"], "Yes") == "Yes":
			tags = Query.query_array("Update tags.")
			collection.update_one({"_id": _id}, \
				{"$set": {"tags": tags}})

		if Query.query_option("Update similar?", ["Yes", "No"], "Yes") == "Yes":
			similar = Query.query_array("Update similar.")
			collection.update_one({"_id": _id}, \
				{"$set": {"similar": similar}})

		if Query.query_option("Update solutions?", ["Yes", "No"], "Yes") == "Yes":
			solutions = Query.query_array("Update solutions.", True)
			collection.update_one({"_id": _id}, \
				{"$set": {"solutions": solutions}})

	@staticmethod
	def delete(collection):
		# TODO: soft delete (enable restore) and hard delete
		_id = Query.query_line("Question ID:")

		entry = collection.find_one({"_id": _id})
		Printer.print_entry_file(entry)

		if Query.query_option("Delete?", ["Yes", "No"], "Yes") == "Yes":
			collection.delete_one({"_id": _id})
