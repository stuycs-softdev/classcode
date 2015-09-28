from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        uname = request.form['username']
        pword = request.form['password']
        button = request.form['button']
        if button=="cancel":
            return render_template('login.html')

        # if we get here, we have the uname and pword
        # to try to authenticate
        if utils.authenticate(uname,pword):
            return "<h1>Logged in</h1>"
        else:
            error="Invalid user or password"
            return render_template("login.html",err=error)

@app.route("/")
def index():
    return render_template("index.html",args = request.args)



if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
