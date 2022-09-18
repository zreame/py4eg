from ctypes.wintypes import tagSIZE
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# test site -> http://www.dr-chuck.com/page1.htm
# test site -> http://www.dr-chuck.com/page2.htm
url = input('Enter - ')
html = urllib.request.urlopen(url).read()

# beautifulsoup handles all the imperfections in the html code and gives back what we need
soup = BeautifulSoup(html, 'html.parser')

# checkout beautiful soup docs, will take some time

# Retrieve all anchor tags, then printing th hrefs within an anchor tag
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))
