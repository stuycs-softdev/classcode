from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['button']
        uname=request.form['username']
        pword=request.form['password']
        if button=="cancel":
            return render_template("login.html")
        # if we're here we should have
        # a username and password
        if utils.authenticate(uname,pword):
            return "You're in"
        else:
            return render_template("login.html",error="INVALID USERNAME OR PASSWORD")

    
@app.route("/")
def index():
    #print request
    #print dir(request)
    #print "SEPERATOR"
    print request.args
    return render_template("index.html",args = request.args)



if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
