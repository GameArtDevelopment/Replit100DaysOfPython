from flask import Flask, render_template, request, redirect, session
import os
from replit import db

app = Flask(__name__, static_url_path="/static")
app.secret_key = my_secret = os.environ['secretKey']

userid = 'username'


def getBlogs():
    entry = ""
    f = open("entry.html", "r")
    entry = f.read()
    f.close()
    keys = db.keys()
    keys = keys.reverse()
    content = ""
    for key in reversed(keys):
        thisEntry = entry
        if key != "user":
            thisEntry = thisEntry.replace("{title", db[key]["title"])
            thisEntry = thisEntry.replace("{date", db[key]["date"])
            thisEntry = thisEntry.replace("{body", db[key]["body"])
            content += thisEntry
    return content


@app.route('/')
def index():
    if userid == 'username':
        return redirect("/edit")
    page = ""
    f = open("feed.html", "r")
    page = f.read()
    page = page.replace("{content}", getBlogs())
    f.close()
    return page


@app.route("/loginForm")
def loginForm():
    if userid == 'username':
        return redirect("/edit")
    page = ""
    f = open("login.html", "r")
    page = f.read()
    page = page.replace("{content}", getBlogs())
    f.close()
    return page


@app.route('/login', methods=["POST"])
def login():
    if userid == 'username':
        return redirect("/edit")
    form = request.form
    if form["username"] == db["use"]["username"] and form["password"] == db["user"]["password"]:
        session["user"] = True
        return redirect("/edit")
    else:
        return redirect("/loginForm")


@app.route("/edit")
def edit():
    if not userid == 'username':
        return redirect("/")
    page = ""
    f = open("edit.html", "r")
    page = f.read()
    page = page.replace("{content}", getBlogs())
    f.close()
    return page


@app.route("/add", methods=["POST"])
def add():
    form = request.form
    entry = {"title": form["title"],
             "date": form["date"], "body": form["body"]}
    db[form["date"]] = entry
    return redirect("/edit")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


app.run(host='0.0.0.0', port=81)
