# Description: Create a login and signup page using Flask and Redis
# This code works using Replit.com's built-in Redis database.
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/signup', methods=["POST"])
def create_user():
    keys = db.keys()
    form = request.form
    if form["username"] in keys:
        db[form["username"]] = {"name": form["name"], "password": form["password"]}
        return redirect ("/signup")
    else:
        return redirect ("/signup")
    
@app.route('/login', methods=["POST"])
def login():
    keys = db.keys()
    form = request.form
    if form["username"] in keys:
        if db[form["username"]]["password"] == form["password"]:
            return "You are logged in."
        else:
            return f"""hello {db[form["username"]]["name"]}, """
    else:
        return redirect ("/login")
    
@app.route('/home')
def home():
    page = ""

app.route('/login')
def login():
    page = """
    <form action="/login" method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>"""
    return page

@app.route('/signup')
def signup():
    page = """
    <form action="/signup" method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Sign Up">
    </form>"""
    return page


@app.route('/')
def index():
    page = """
    <p><a href="/signup">Sign Up</a></p>
    <p><a href="/login">Login</a></p>"""
    return page

app.run(host='0.0.0.0', port=81, debug=True)