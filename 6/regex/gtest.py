import google, urllib2, bs4, re
q="penguins"
pages = google.search(q,num=10,start=0,stop=10)

plist = []
for r in pages:
    plist.append(r)

url = urllib2.urlopen(plist[8])
#print url
page = url.read().decode('ascii')
#print page
soup = bs4.BeautifulSoup(page)
raw = soup.get_text(page)
text = re.sub("[\t\n ]+",' ',raw)
print text

    
