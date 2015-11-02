import urllib2

#url="http://www.weather.com/weather/today/l/10001:4:US"

key="ecdb9f3fb43f5f8663867db2633c7638"

url = "http://api.openweathermap.org/data/2.5/weather?q=NYC&units=Imperial&appid=%s"%(key)

print url
request = urllib2.urlopen(url)
result = request.read()
print result
