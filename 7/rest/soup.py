import urllib2
from bs4 import BeautifulSoup

url="http://www.nytimes.com"

request = urllib2.urlopen(url)
result = request.read()
soup = BeautifulSoup(result,'html.parser')
#print soup.prettify()
for r in soup.find_all("h2"):
    print r
