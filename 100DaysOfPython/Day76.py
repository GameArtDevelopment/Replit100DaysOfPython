# I need to come back to this one. I'm not sure what I'm doing wrong.
from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return 'Hello from Flask'


app.run(host='0.0.0.0', port = 81)