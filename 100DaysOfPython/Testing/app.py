from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_data', methods=['POST'])
def get_data():
    # Example: Interacting with a public API
    api_url = "https://api.publicapis.org/entries"
    response = requests.get(api_url)
    data = response.json()

    # Extract useful information
    entries = data.get('entries', [])
    return render_template('data.html', entries=entries)


if __name__ == '__main__':
    app.run(debug=True)
