from flask import Flask

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return "<h1>Home Page</h1><h2>Hello World</h2>"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
    
