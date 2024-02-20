from flask import render_template
from taskmanager import app, ab

@app.route("/")
def home():
    return render_template("base.html")