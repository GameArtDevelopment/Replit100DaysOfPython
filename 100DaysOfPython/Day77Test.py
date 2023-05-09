from flask import Flask
import datetime
app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    today = datetime.date.today()
    page = f"""<html>
    <head>
    <title>Index</title>
    </head>
    <body>
    <h1>Joseph's Index</h1>
    <p>This is my index page.</p>
    <p>Today's date is {today}</p>
    <p><a href="/home">Home Page</a></p>
    </body>
    </html>"""
    return page

@app.route("/home")
def home():
    today = datetime.date.today()
    page = f"""<html>
    <head>
    <title>Home</title>
    </head>
    <body>
    <h1>Joseph's Home</h1>
    <p>{today}</p>
    <p>This is my home page.</p>
    </body>
    </html>"""
    return page

