from flask import Flask, render_template

app = Flask(__name__)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/oldabout")
def oldaboutpage():
    page="""
<h1>About</h1>
<br>
<ol>
<li>About 1</li>
<li>About 2</li>
<li>About 3</li>
</ol>
"""
    return page

@app.route("/person")
@app.route("/person/")
@app.route("/person/<lastname>")
@app.route("/person/<lastname>/<firstname>")
def person(lastname="",firstname=""):
    if lastname!="zamansky":
        error="WRONG NAME, TRY AGAIN"
    else:
        error="YOU WIN"
    d = {'last':lastname,
         'first':firstname,
         'title':"Fool Pitier",
         'error':error}

    l = [10,20,31,45,1234,'hello','item',22]
    
    return render_template("person.html",d=d,list=l)

@app.route("/lucky")
def lucky_number():
    import random
    r = random.randrange(1,100)
    # return "<h1>Lucky Number: %d</h1>" % (r)
    return render_template("lucky.html",number=r)
    
@app.route("/home")
@app.route("/")
def kerfuffle():
    page="""
    <h1>Home Page</h1><h2>Hello World</h2>
    <hr>
    <button><a href="/about">about</a></button>
"""
    return page


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
    
