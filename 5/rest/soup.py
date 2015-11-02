import urllib2
from bs4 import BeautifulSoup

url="https://www.nytimes.com"

request = urllib2.urlopen(url)
result = request.read()
soup = BeautifulSoup(result,'html.parser')

for a in soup.find_all('h3'):
    print a
