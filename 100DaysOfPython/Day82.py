from flask import Flask, request

app = Flask(__name__)

@app.route("/language", methods = ["GET"])
def lang():
  data = request.args
  if data  == {}:
    return "Nothing to see here"
  if data["lang"] == "eng":
    return "Hello, and welcome to my website"
  elif data["lang"] == "ger":
    return "Wilkommen auf meiner Webseite"

@app.route("/")
def index():
  return "Hello from my simple flask website"


app.run(host="0.0.0.0", port=81)

# Day 82 of #100DaysOfCode
# Today I learned how to use the request module in Flask to get data from the URL



