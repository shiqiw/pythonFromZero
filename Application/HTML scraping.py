# install pip tool
# then lxml and requests
# all used sudo

# scrape content from here
# http://docs.python-guide.org/en/latest/scenarios/scrape/

# from lxml import html
# import requests

# base = 'http://zh.harrypotter.wikia.com'
# page = requests.get(base + '/wiki/%E9%AD%94%E6%9D%96%E6%9C%A8%E6%9D%90')
# tree = html.fromstring(page.content)

# rows = tree.xpath('//table[@class="wikitable"]/tr/td')
# # first row is headers, not informative
# rows = rows[1:]

# for row in rows:
# 	print row.td.text_content()


# after reading blogs, decide to switch to beautiful soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from BeautifulSoup import BeautifulSoup
import random
from sets import Set
import sys
from urllib2 import HTTPError
from urllib2 import urlopen

def QueryUpdate(question, target):
	sys.stdout.write("=> " + question + " (default no)\n")
	sys.stdout.write("   Yes\n")
	sys.stdout.write("   No\n")
	
	yesOption = Set(['YES', 'Y'])
	choice = raw_input().upper()
	if choice in yesOption:
		sys.stdout.write("Start to update {0}.\n".format(target))
		return True
	else:
		return False

def GetWoodInfo():
	base = 'http://zh.harrypotter.wikia.com'
	soup = BeautifulSoup(urlopen(base + '/wiki/%E9%AD%94%E6%9D%96%E6%9C%A8%E6%9D%90').read())

	section = soup.find('section', id='WikiaPage')
	rows = section.find('table', {"class": "wikitable"}).findAll('tr')[1:-1]
	wood = open("Wand wood.txt", "w")

	for row in rows:
	    column = row.findAll('td')[0]
	    name = column.find('a').get('title').strip().encode('utf-8')
	    link = base + column.find('a').get('href')

	    try:
	    	subsoup = BeautifulSoup(urlopen(link).read())
	    	meta = subsoup.find('meta', {"property": "og:description"})
	    	# .strip() remove newline and space
	    	description = meta.get('content').strip().encode('utf-8')
	    	# should use string format here
	    	wood.write("{0}\n{1}\n\n".format(name, description))
	    except HTTPError:
	    	print name
	    	print HTTPError

	wood.close()
	return

def GetCoreInfo():
	base = 'http://zh.harrypotter.wikia.com'
	soup = BeautifulSoup(urlopen(base + '/wiki/%E6%9D%96%E8%8A%AF').read())

	section = soup.find('section', id='WikiaPage')
	rows = section.find('table', {"class": "wikitable"}).findAll('tr')[1:-1]
	core = open("Wand core.txt", "w")

	for row in rows:
		name  = row.findAll('td')[0].find('a').get('title').strip().encode('utf-8')

		usageColumn = row.findAll('td')[3]
		usage = usageColumn.renderContents().strip()
		if usageColumn.find('p') != None:
			usage = usageColumn.find('p').getText().strip().encode('utf-8')

		# indentation really matters
		core.write("{0}\n{1}\n\n".format(name, usage))

	core.close()
	return

def GetWandInfo():
	# this is not recommended for huge files
	# list index is zero based?
	woodChoice = open("Wand wood.txt", 'r').readlines()
	random.seed()
	choicew = random.randint(0, len(woodChoice)/3)*3

	coreChoice = open("Wand core.txt", 'r').readlines()
	random.seed()
	choicec = random.randint(0, len(coreChoice)/3)*3

	final = open("Wand.txt", "w")
	final.write(woodChoice[choicew])
	final.write(woodChoice[choicew+1])
	final.write('+\n')
	final.write(coreChoice[choicec])
	final.write(coreChoice[choicec+1])
	final.close()

	sys.stdout.write("Your wand information is available now:\n")
	sys.stdout.write("{0}+\n{1}\n".format(woodChoice[choicew], coreChoice[choicec]))
	return

def Main():
	if QueryUpdate("Download the newest wand wood info?", "Wand wood"):
		GetWoodInfo()

	if QueryUpdate("Download the newest wand core info?", "Wand core"):
		GetCoreInfo()

	GetWandInfo()

Main()