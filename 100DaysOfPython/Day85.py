# Description: Create a login and signup page using Flask and Redis
# This code works using Replit.com's built-in Redis database.
import os
from flask import Flask, redirect, request, session
from replit import db

app = Flask(__name__)
app.secret_key = os.environ["sessionKey"]


@app.route('/signup', methods=["POST"])
def create_user():
    if session.get("loggedIn"):
        return redirect("/welcome")
    keys = db.keys()
    form = request.form
    if form["username"] in keys:
        db[form["username"]] = {
            "name": form["name"],
            "password": form["password"]
        }
        return redirect("/signup")
    else:
        return redirect("/signup")


@app.route('/login', methods=["POST"])
def login():
    if session.get("loggedIn"):
        return redirect("/welcome")
    keys = db.keys()
    form = request.form
    if form["username"] in keys:
        if db[form["username"]]["password"] == form["password"]:
            session["loggedIn"] = form["username"]
            return redirect("/welcome")
        else:
            return f"""hello {db[form["username"]]["name"]}, """
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")

@app.route('/welcome')
def welcome():
    page = f"""<h1>Welcome {db[session["loggedIn"]]["name"]}</h1>
    <button type="button" onClick="location.href='/logout'">Log out</button>"""
    return page


app.route('/login')


def login():
    if session.get("loggedIn"):
        return redirect("/welcome")
        page = """
    <form action="/login" method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>"""
        return page


@app.route('/signup')
def signup():
    if session.get("loggedIn"):
        return redirect("/welcome")
    page = """
    <form action="/signup" method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Sign Up">
    </form>"""
    return page


@app.route('/')
def index():
    if session.get("loggedIn"):
        return redirect("/welcome")
    page = """
    <p><a href="/signup">Sign Up</a></p>
    <p><a href="/login">Login</a></p>"""
    return page


app.run(host='0.0.0.0', port=81, debug=True)