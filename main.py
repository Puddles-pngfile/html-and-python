from flask import Flask, redirect, url_for, render_template
import random



app = Flask(__name__)

@app.route("/")
def home():
    name = "i lick toes"
    return render_template("index.html", content=name)

@app.route("/aboutme")
def aboutme():
    rand = random.randint(0,100)
    return render_template("aboutme.html", rand = rand )





if __name__ == "__main__":
    app.run(debug=True)





  