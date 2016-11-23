from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
from urllib2 import urlopen
import json

# pip instll enum34
# from enum import Enum

# Animal = Enum('Cat', 'Dog')

# without import
class Operation(object):
	CREATE = 1
	READ = 2
	UPDATE = 4
	DELETE = 8
	EXIT = 16
	PASS = 32

	# https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
	# can be simplified, just make use of class method
	@classmethod
	def decide_operation(cls, option):
		if option.startswith("a"):
			return cls.CREATE
		elif option.startswith("f"):
			return cls.READ
		elif option.startswith("s"):
			return cls.UPDATE
		elif option.startswith("d"):
			return cls.DELETE
		elif option.startswith("e"):
			return cls.EXIT
		else:
			return cls.PASS

	@staticmethod
	def create_operation(posts):
		# exception in initAndListen: 29 Data directory /data/db not found. terminating
		# sudo mkdir -p /data/db ==> create dir at root
		# lhttps://gist.github.com/adamgibbons/cc7b263ab3d52924d83b ==> set permission

		post = Entry.new_entry()
		# duplicate key _id insertion will throw error
		post_id = posts.insert_one(post).inserted_id
		print "Add a new entry %s" %(post_id)

	def read_operation(posts):
		# should have 0 and 1 entry now.
		# 0 is fake record, 1 is a valid record

		# make entries a set
		entries = []

		_id = raw_input("id:\n>>")
		if _id != "":
			entry = posts.find_one({"_id": _id})

		Entry.read_entry(entries)

class Entry(object):
	@staticmethod
	def new_entry():
		# store info in dictionary, pymongo does not require json
		entry = {}

		while True:
			_id = raw_input("_id:\n>>").strip()
			if _id != "":
				entry["_id"] = _id
				break

		while True:
			title = raw_input("title:\n>>").strip()
			if title != "":
				entry["title"] = title
				break

		try:
			# try scrape question description
			base = "https://leetcode.com/problems/"
			seg = "-".join(title.split())
			url = base + seg + "/"
			soup = BeautifulSoup(urlopen(url).read())
			description = soup.find("head").find("meta", {"name": "description"})

			parser = HTMLParser()
			readable = parser.unescape(description.get("content"))
			entry["content"] = readable

			# try scrape tags at the same time
			anchors = soup.find("span", {"class": "hidebutton"}).findAll("a")
			tags = []
			for anchor in anchors:
				tags.append(anchor.getText())
			entry["tags"] = tags
		except:
			print "Unable to scrape content online"
			readable = raw_input("content:\n>>")
			entry["content"] = readable

			tags = []
			while True:
				tag = raw_input("tag:\n>>").strip()
				if tag != "":
					tags.append(tag)
				else:
					break

		#should be a list
		company = raw_input("company:\n>>").strip()
		entry["company"] = company


		thought = raw_input("thought:\n>>").strip()
		entry["thought"] = thought

		record = raw_input("pass: y)es n)o\n>>")
		entry["passRecord"] = record

		#return json.dumps(entry)
		return entry

		def read_entry(entries):
			for entry in entries:
				# each entry is a dictionary
				print "%s. %s\n" %(entry["_id"], entry["title"])
				print entry["content"]
				raw_input("want to show tags?\n")
				# is it a list, how to print list properly
				print entry["tags"]
				raw_input("want some hint?\n")
				print entry["thought"]
