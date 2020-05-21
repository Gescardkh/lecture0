from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

#@app.route("/<string:name>")
#def hello(name):
    #name=name.capitalize()
    #return f"Hello, {name}"

@app.route("/hello", methods=["Post"])
def hello():
    name=request.form.get("name")
    return render_template("hello.html",name=name)
