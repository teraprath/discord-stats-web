# Discord Stats Web
# Author: https://github.com/teraprath

from typing import NoReturn
from flask import Flask, render_template, redirect, request, url_for
import database as db

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    list = db.list()
    list.sort(reverse=False, key=lambda list: list[7])
    counter = len(list)
    rank = True
    username = None
    if request.method == "POST":
        username = request.form["username"]
        list = db.list_with(username)
        if not list == []:
            rank = False
        else:
            list = []

    return render_template("index.html", list=list, counter=counter, username=username)

if __name__ == "__main__":
    app.run(port=5500, debug=True)