# Some fc2 blog require password
# use selenium driver 
# the rest is normal scraping

# from selenium import webdriver

# # initiate
# driver = webdriver.Firefox() # initiate a driver, in this case Firefox
# driver.get("http://example.com") # go to the url

# # log in
# username_field = driver.find_element_by_name(...)) # get the username field
# password_field = driver.find_element_by_name(...)) # get the password field
# username_field.send_keys("username") # enter in your username
# password_field.send_keys("password") # enter in your password
# password_field.submit() # submit it

# # print HTML
# html = driver.page_source
# print html

# want to download html as well

# this extract only work for 2 blogs
# want to extract related page as well

from BeautifulSoup import BeautifulSoup, NavigableString, Tag
import sys
from urllib2 import urlopen

sys.stdout.write("Please provide fc2 blog url:\n")
url = raw_input()

if url == "":
	url = "skdusk.blog126.fc2blog.us/blog-entry-2518.html"
if not url.startswith("http://"):
	url = "http://" + url

soup = BeautifulSoup(urlopen(url).read())

filename = soup.find('head').find('title').getText()
f = open(filename + ".txt", "w")

# fc2 usually store text content in div, linebreak with <br/>
# need to navigate through tree
# need to prettify
div = soup.find('div', id='more')
for br in div.findAll('br'):
	next = br.nextSibling
	while (next and isinstance(next, NavigableString)):
		#print unicode(next).decode('unicode-escape')
		f.write(next.strip().encode('utf-8'))
		f.write('\n\n')
		next = next.nextSibling

f.close()