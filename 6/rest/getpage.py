import urllib2
import json

#url = "https://www.google.com/#safe=off&q=iguana"
url='http://api.openweathermap.org/data/2.5/weather?q="nyc"&appid=ecdb9f3fb43f5f8663867db2633c7638&units=imperial'


request = urllib2.urlopen(url)
result = request.read()
r = json.loads(result)
print r
print
print r.keys()
print r['main']
print r['main']['temp']
