from flask import Flask, render_template
from flask import Markup

app = Flask(__name__)

@app.route("/include")
def include():
    l="""
    <ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    </ol>
<script>
alert("HELLO WORLD");
</script>
    """
    #l = Markup(l)
    return render_template("include.html",list=l)

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
