from flask import Flask, redirect, url_for, render_template
import random
app = Flask(__name__)


@app.route('/')
def home():
    name = "Verge"
    return render_template("index.html")

@app.route("/rng")
def numgen():
    rand = random.randint(0,1000)
    return render_template("randnum.html")

 

if __main__ == "__name__":
    app.run()








