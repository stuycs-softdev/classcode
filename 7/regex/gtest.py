import google, urllib2, bs4, re

q="who played spiderman"

results = google.search(q,num=10,start=0,stop=10)

rlist = []
for r in results:
    rlist.append(r)

url = urllib2.urlopen(rlist[0])
page = url.read()
soup = bs4.BeautifulSoup(page,'html')
raw = soup.get_text()

text = re.sub("[ \t\n]+"," ",raw)
print text
