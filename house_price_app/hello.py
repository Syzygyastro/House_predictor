from flask import current_app as app
from flask import Flask, render_template

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/forum")
def index_forum():
    return "forum page"