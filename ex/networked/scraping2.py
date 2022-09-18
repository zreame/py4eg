import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# handles websites with ssl (https), this block of code ignores ssl cert errors, checkout stackoverflow
# not that the websites are bad but py does not recognise the ssl certs (not in py's official list), so it returns error wo this block
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# try https://www.si.umich.edu/
# try http://www.dr-chuck.com/
url = input('Enter - ')

# .read() returns entire doc in a big string with newlines at the end of each line, instead of line by line
# urllib handles encoding
# context to handle ssl cert error
html = urllib.request.urlopen(url, context=ctx).read()
# print('html', html)

# bs4 knows how to handle both utf8 and unicode, no decode() needed
# bs4 is a complex library for scraping, read docs
# we can use regex etc but there are so many inconsistencies in html, so we use bs4

soup = BeautifulSoup(html, 'html.parser')
# print('soup', soup)

tags =  soup('a')
for tag in tags :
    print(tag.get('href', None))
