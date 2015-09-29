from flask import Flask, render_template, session
from flask import redirect, url_for

app = Flask(__name__)

@app.route("/reset")
def reset():
    session['n']=0
    #return redirect("/inc")
    return redirect(url_for("inc"))


@app.route("/inc")
def inc():
    if 'n' not in session:
        session['n']=0
    n = session['n']
    n=n+1
    session['n']=n
        
    return render_template("counter.html",n=n)

@app.route("/dec")
def dec():
    if 'n' not in session:
        session['n']=0
    n = session['n']
    n=n-1
    session['n']=n
        
    return render_template("counter.html",n=n)

@app.route("/")
def index():
    return "hello"



if __name__ == "__main__":
   app.debug = True
   app.secret_key = "Don't store this on github"
   app.run(host="0.0.0.0", port=8000)
