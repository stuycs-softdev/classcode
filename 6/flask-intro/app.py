from flask import Flask, render_template

app = Flask(__name__)


@app.route("/lucky")
def lucky():
    import random
    r = random.randrange(1,100)
    return render_template("lucky.html",number=r)


@app.route("/p")
@app.route("/p/")
@app.route("/p/<lastname>")
@app.route("/p/<lastname>/<firstname>")
def person(lastname="",firstname=""):
    
    d = {"last":lastname,
         'first':firstname}
    d['title']="Grand Poobah"
    l=[10,"twenty",30,"forty"]
    return render_template("person.html",d = d, l = l)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/oldabout")
def oldabout():
    page="""
<h1>About</h1>
<hr>
<ol>
<li>Fred Flintstone</li>
<li>Mr. T</li>
<li>The Hulk</li>
</ol>
"""
    return page

@app.route("/")
@app.route("/home")
def home():
    page = """
    <h1>Hello World</h1><h2>main page</h2>
<button><a href="/about">About</a></button>
"""
    return page

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
    
    
