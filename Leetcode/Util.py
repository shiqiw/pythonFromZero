import BeautifulSoup
import HTMLParser 
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
	def print_header(cls, *args):
		content = ". ".join(args)
		print Printer.BOLD + content + Printer.ENDC

	@classmethod
	def print_code(cls, content):
		# TODO: deal with /* */ comment
		# TODO: deal with built-in types
		lines = content.split('\n')
		for line in lines:
			if "//" in line:
				print Printer.OK + line + Printer.ENDC
			else:
				print line

	@classmethod
	def print_entry(cls, entry):
		# TODO: provide option to not print tags, similar and solutions
		# TODO: real mode, or get ride of entry content dependency
		Printer.print_header(entry["_id"], entry["title"])
		print entry["description"]

		raw_input(Printer.BOLD + "Show tags?" + Printer.ENDC)
		for tag in entry["tags"]:
			print tag

		raw_input(Printer.BOLD + "Show similar?" + Printer.ENDC)
		for similar in entry["similar"]:
			print similar

		raw_input(Printer.BOLD + "Show solution?" + Printer.ENDC)
		for solution in entry["solutions"]:
			Printer.print_code(solution)

def query_option(question, options, default):
	# TODO: change options from list to dictionary
	formated_options = []
	mapped_options = {}
	for option in options:
		formated_options.append(option[0].upper() + ")" + option[1:])
		mapped_options[option[0].upper()] = option

	formated_default = default[0].upper() + ")" + default[1:]

	while True:
		# http://stackoverflow.com/questions/3263672/python-the-difference-between-sys-stdout-write-and-print
		sys.stdout.write("=> " + question + "\n")

		for key in formated_options:
			sys.stdout.write("   " + key + "\n")
			
		sys.stdout.write("   Default: " + default + "\n")
		sys.stdout.write("   Input your choice or ENTER to default: ")

		choice = raw_input().upper()
		if default is not None and choice == "":
			return default
		elif choice in mapped_options:
			return mapped_options[choice]
		else:
			Printer.print_error("   Oops. Cannot quite understand. Let's try again.\n")

def query_paragraph(question = None):
	if question != None:
		sys.stdout.write("=> " + question + "\n")
		sys.stdout.write("   (Please use ':wq' as exit.)\n")

	lines = []

	while True:
		line = raw_input()
		if line != ":wq":
			lines.append(line)
		else:
			return '\n'.join(lines)

def query_array(question, paragraph = False, prevs = []):
	# TODO: provide cancel option
	sys.stdout.write("=> " + question + "\n")

	ret = []
	para = ""

	for i in range(0, len(prevs)):
		Printer.print_code(prevs[i])
		if query_option("Modify?", ["Yes", "No"], "No") == "Yes":
			if paragraph:
				para = query_paragraph()
			else:
				para = raw_input()
			if para != "":
				ret.append(para)
		else:
			ret.append(prevs[i])

	while True:
		if query_option("Add more?", ["Yes", "No"], "Yes") == "Yes":
			if paragraph:
				para = query_paragraph()
			else:
				para = raw_input()
			if para != "":
				ret.append(para)
		else:
			break

	return ret

class Column(object):
	DESCRIPTION = 1
	TAGS = 2
	SIMILAR = 4

def scrape_content(title, tag, attribute, column):
	# TODO: scrape content where password is needed
	# TODO: catch exception when tags or similar is missing
	# sometimes it will forbidden, like No.96

	# http://stackoverflow.com/questions/7002206/expected-buffer-object-error-on-string-translate-python-2-6
	chars_to_remove = "'\'()"
	title = title.translate(None, chars_to_remove).replace('-', ' ')
	path = "-".join(title.split())
	url = "https://leetcode.com/problems/" + path + "/"
	soup = BeautifulSoup.BeautifulSoup(urlopen(url).read())
	content = soup.findAll(tag, attribute)

	if column == Column.DESCRIPTION:
		# meta => name=description
		parser = HTMLParser.HTMLParser()
		return parser.unescape(content[0].get("content"))
	elif column == Column.TAGS:
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
