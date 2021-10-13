from flask import Flask, render_template, redirect, url_for
import database as db

app = Flask(__name__)

@app.route("/")
def index():
    list = db.list()
    return render_template("index.html", list=list)

if __name__ == "__main__":
    app.run(port=5500, debug=True)