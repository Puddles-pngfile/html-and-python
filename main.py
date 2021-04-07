from flask import Flask, redirect, url_for, render_template
import random



app = Flask(__name__)

@app.route("/")
def home():
    name = "Useless Website"
    return render_template("index.html", content=name)

@app.route("/randnum")
def randnum():
    rand = random.randint(0,100)
    return render_template("randnum", rand = rand )
    




if __name__ == "__main__":
    app.run(debug=True)





  