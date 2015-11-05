import urllib2,json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/t")
@app.route("/t/<tag>")
def t(tag="penguins"):
    key="6qjbDDaQ4vUogvpFIZ2UoaHuo6ykn1vMpjRYOdYOPCQI6dBw4K"
    url="https://api.tumblr.com/v2/tagged?tag=%s&api_key=%s"
    url=url%(tag,key)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    # r['response'][1]['photos'][0]['original_size']['url']
    photos=[]
    for item in r['response']:
        try:
            photos.append(item['photos'][0]['original_size']['url'])
        except:
            pass

    return render_template("photos.html",urls = photos)

    
@app.route("/")
def index():
    return "hello"



if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)






