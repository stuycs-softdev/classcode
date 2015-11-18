import urllib2, google, bs4, re

q="who played spiderman"
r = google.search(q,num=10,start=0,stop=10)
l=[]
for result in r:
    l.append(result)

print l[0]

u = urllib2.urlopen(l[0])
page = u.read()
#print page
soup = bs4.BeautifulSoup(page)
raw = soup.get_text()
#print raw
text = re.sub("[\t\n ]"," ",raw)
print text 
