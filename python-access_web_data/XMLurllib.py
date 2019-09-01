#  extract an xml from the given website and display the sum of the values present in count tag of comment elements present in that xml
# URL: http://py4e-data.dr-chuck.net/comments_254940.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location:')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
group = ET.fromstring(data)
tags = group.findall('comments/comment')
sum = 0
for tag in tags:
    sum = sum + int(tag.find('count').text)
print(sum)