import BeautifulSoup
from difflib import SequenceMatcher
import HTMLParser 
import os
import re
import sys
from urllib2 import urlopen

class Printer:
	ENDC = '\033[0m'
	BOLD = '\033[1m' 		# bold
	UNDERLINE = '\033[4m'	# underline
	TEST = '\033[7m'		# black bacground
	ERROR = '\033[91m'		# red
	OK = '\033[92m'			# green
	WARNING = '\033[93m'	# yellow
	PURPLE = '\033[94m'		# purple
	PINK = '\033[95m'		# pink

	@classmethod
	def print_normal(cls, content):
		print content

	@classmethod
	def print_ok(cls, content):
		print Printer.OK + content + Printer.ENDC

	@classmethod
	def print_warning(cls, content):
		print Printer.WARNING + content + Printer.ENDC

	@classmethod
	def print_error(cls, content):
		print Printer.ERROR + content + Printer.ENDC

	@classmethod
	def print_bold(cls, content):
		print Printer.BOLD + content + Printer.ENDC

	@classmethod
	def print_underline(cls, content):
		print Printer.UNDERLINE + content + Printer.ENDC

	@classmethod
	def print_header(cls, *args):
		content = ". ".join(args)
		print Printer.print_bold(content)

	@classmethod
	def print_code(cls, content):
		# TODO: deal with built-in types
		# TODO: deal with comment in other languages
		lines = content.split('\n')
		comment = False
		for line in lines:
			# sinle line comment in Java
			if "//" in line:
				print Printer.PURPLE + line + Printer.ENDC
			# multiple line comment in Java
			elif "/*" in line:
				comment = True
				print Printer.PURPLE + line + Printer.ENDC
			elif "*/" in line:
				print Printer.PURPLE + line + Printer.ENDC
				comment = False
			else:
				if comment == True:
					print Printer.PURPLE + line + Printer.ENDC
				else:
					print line

	@classmethod
	def print_entry_console(cls, entry):
		Printer.print_header(entry["_id"], entry["title"])
		print entry["description"]

		if Query.query_option("Show company?", ["Yes", "No"], "Yes") == "Yes":
			if "company" in entry:
				for company in entry["company"]:
					print company

		if Query.query_option("Show tags?", ["Yes", "No"], "Yes") == "Yes":
			if "tags" in entry:
				for tag in entry["tags"]:
					print tag

		if Query.query_option("Show similar?", ["Yes", "No"], "Yes") == "Yes":
			if "similar" in entry:
				for similar in entry["similar"]:
					print similar

		if Query.query_option("Show solution?", ["Yes", "No"], "Yes") == "Yes":
			count = 1
			for solution in entry["solutions"]:
				Printer.print_underline("Solution " + str(count))
				Printer.print_code(solution)

	@classmethod
	def print_multi_entry_console(cls, entries):
		for entry in entries:
			if Query.query_option("Continue?", ["Yes", "No"], "Yes") == "No":
				break
			Printer.print_clear()
			Printer.print_entry_console(entry)

	@classmethod 
	def print_entry_file(cls, entry):
		# Put print to file here just for convenience
		filename = ". ".join([entry["_id"], entry["title"]])
		target = open(filename+".txt", 'w')

		target.write(filename)
		
		target.write("\n")
		target.write(entry["description"])

		target.write("\n\nCompany:")
		if "company" in entry:
			for company in entry["company"]:
				target.write("\n")
				target.write(company)

		target.write("\n\nTags:")
		if "tags" in entry:
			for tag in entry["tags"]:
				target.write("\n")
				target.write(tag)

		target.write("\n\nSimilar:")
		if "similar" in entry:
			for similar in entry["similar"]:
				target.write("\n")
				target.write(similar)

		target.write("\n\nSolution:")
		for solution in entry["solutions"]:
			target.write("\n")
			target.write(solution)

	@classmethod
	def print_clear(cls):
		# Put clear console here just for convenience
		# ctrl+K is the real claer history in mac
		clear = lambda: os.system("clear")
		clear()

class Query:
	@classmethod
	def query_option(cls, question, options, default):
		"""
		Display question with option to choose from.
		Type: string, list<string>, string
		Return type: string
		"""
		formated_options = []
		mapped_options = {}
		for option in options:
			# format to O)ption
			formated_options.append(option[0].upper() + ")" + option[1:])
			# look up O => option
			mapped_options[option[0].upper()] = option
		formated_options.sort()

		while True:
			# http://stackoverflow.com/questions/3263672/python-the-difference-between-sys-stdout-write-and-print
			Printer.print_bold("=> " + question)

			for key in formated_options:
				Printer.print_normal("   " + key)
				
			Printer.print_normal("   Default: " + default)
			Printer.print_normal("   Input your choice or ENTER to default: ")

			choice = raw_input().upper()
			if default is not None and choice == "":
				return default
			elif choice in mapped_options:
				return mapped_options[choice]
			else:
				Printer.print_error("   Oops. Cannot quite understand. Let's try again.")

	@classmethod
	def query_line(cls, question = None):
		"""
		Read single line console input.
		Use :q! as discard code.
		Type: string
		Return type: string
		"""
		if question != None:
			Printer.print_bold("=> " + question)

		line = raw_input()
		if line == ":q!":
			return ""
		else:
			return line

	@classmethod
	def query_paragraph(cls, question = None):
		"""
		Read multiple line console input.
		Use :wq as exit code, use :q! as discard code.
		Type: string
		Return type: string
		"""
		if question != None:
			Printer.print_bold("=> " + question)

		lines = []

		while True:
			line = Query.query_line()
			if line != ":wq":
				lines.append(line)
			else:
				return '\n'.join(lines)

	@classmethod
	def query_array(cls, question, paragraph = False):
		"""
		Prompt for multiple user input. Each as a separate entry.
		Use :q! as discard current entry code.
		Type: string, boolean
		Return type: list<string>
		"""
		Printer.print_bold("=> " + question)
		if paragraph == True:
			Printer.print_normal("   (Please use ':wq' to exit.)")
		else:
			Printer.print_normal("   (Please use ':q!' to discard.)")

		ret = []
		para = ""
		
		if paragraph:
			para = Query.query_paragraph()
		else:
			para = Query.query_line()

		while para != "":
			ret.append(para)
			if Query.query_option("Add more?", ["Yes", "No"], "Yes") == "Yes":
				if paragraph:
					para = Query.query_paragraph()
				else:
					para = Query.query_line()
			else:
				para = ""

		return ret

class Scraper:
	DESCRIPTION = 1
	TAGS = 2
	SIMILAR = 4

	@classmethod
	# unbound method scrape_content() must be called with Scraper instance as first argument
	def scrape_content(cls, title, tag, attribute, column):
		# TODO: scrape content where password is needed
		# TODO: investigate forbid scraping mechanism, like No.96
		# why it can return different type?

		# http://stackoverflow.com/questions/7002206/expected-buffer-object-error-on-string-translate-python-2-6
		chars_to_remove = "\'()`"
		title = title.translate(None, chars_to_remove).replace('-', ' ')
		path = "-".join(title.split())
		url = "https://leetcode.com/problems/" + path + "/"
		soup = BeautifulSoup.BeautifulSoup(urlopen(url).read())
		content = soup.findAll(tag, attribute)
		if column == Scraper.DESCRIPTION:
			# meta => name=description
			parser = HTMLParser.HTMLParser()
			return parser.unescape(content[0].get("content"))
		elif column == Scraper.TAGS:
			# span => class=hidebutton
			tags = []
			for anchor in content[0].findAll("a"):
				tags.append(anchor.getText())
			return tags
		else:
			# span => class=hidebutton
			# format is:(*) title
			similar = []
			title = re.compile("\([E|M|H]\) (.*)")
			for anchor in content[1].findAll("a"):
				ans = title.search(anchor.getText())
				similar.append(ans.group(1))
			return similar

class TextAnalyzer:
	"""
	https://en.wikipedia.org/wiki/Hamming_distance
	https://en.wikipedia.org/wiki/Levenshtein_distance
	https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
	https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance

	https://pypi.python.org/pypi/ngram
	https://pythonhosted.org/ngram/ngram.html
	"""

	@classmethod
	def big_gram(cls, str1, str2):
		# http://stackoverflow.com/questions/653157/a-better-similarity-ranking-algorithm-for-variable-length-strings/14631287#14631287
		'''
		Perform bigram comparison between two strings
		and return a percentage match in decimal form
		'''
		pairs1 = get_bigrams(str1)
		pairs2 = get_bigrams(str2)
		intersection = pairs1 & pairs2
		return (2.0 * len(intersection)) / (len(pairs1) + len(pairs2))

	@classmethod
	def get_bigrams(cls, string):
		'''
		Takes a string and returns a list of bigrams
		'''
		s = string.lower()
		return {s[i:i+2] for i in xrange(len(s) - 1)}

	@classmethod
	def sequence_matcher(cls, str1, str2):
		return SequenceMatcher(None, str1, str2).ratio()

	@classmethod
	def ngram(cls, str1, str2):
		#pip install ngram
		#from ngram import NGram
		return NGram.compare(str1, str2)
