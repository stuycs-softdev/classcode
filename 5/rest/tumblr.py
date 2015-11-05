import urllib2,json
from flask import Flask, render_template



app = Flask(__name__)

@app.route("/t")
@app.route("/t/<tag>")
def t(tag="penguin"):
    url = """
    http://api.tumblr.com/v2/tagged?tag=%s&api_key=6qjbDDaQ4vUogvpFIZ2UoaHuo6ykn1vMpjRYOdYOPCQI6dBw4K
    """
    url = url%(tag)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    #r['response'][0]['photos'][0]['original_size']['url']
    photos=[]
    for item in r['response']:
        try:
            newphoto = item['photos'][0]['original_size']['url']
            photos.append(newphoto)
        except:
            pass
    return render_template("tagged.html",urls=photos)

@app.route("/")
def index():
    return "hello"



if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)




