#reading the JSON data from the URL and performing operations; URL: http://py4e-data.dr-chuck.net/comments_254941.json
import urllib.request, urllib.parse, urllib.error
import json
url = input('Enter url - ')
js = urllib.request.urlopen(url).read()
data = js.decode()
try:
    js1=json.loads(data)
except:
    js1 = None
total = 0
for item in js1["comments"]:
    total = total+int(item["count"])
print(total)