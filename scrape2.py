#Updated on 6/11/2014
import requests
import urllib
from BeautifulSoup import BeautifulSoup
import os

#Outputs the entire html source code and prints it
url = 'http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/web/HTMLParser.html'
response = requests.get(url)
html = response.content
print html
raw_input("Press enter to jump to next")
os.system('clear')
soup = BeautifulSoup(html)
print soup.prettify()

raw_input("Press enter to jumo to next")
os.system('clear')
thisurl = 'http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/web/HTMLParser.html'
handle = urllib.urlopen(thisurl)
html_gunk = handle.read()
#print html_gunk
print html_gunk[:150]    #prints the first 150 letter
