# read the html data from the url - http://py4e-data.dr-chuck.net/comments_254938.html  and caluclate the sum of all values in the second part of the table in the html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
addi = 0
for tag in tags:
    addi = addi + int(tag.contents[0])
print(addi)