from flask import Flask, render_template

app = Flask(__name__)

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
    page="<h1>Hello World</h1>"
    page = page + '<button><a href="/about">About</a></button>'
    page = page + "<h2>Welcome</h2>"
    return page
@app.route("/lucky")
def lucky():
    import random
    number = random.randrange(1,100)
    return "<h1>Lucky Number: %d"%(number)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
