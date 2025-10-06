# app.py

from flask import Flask
import requests  # This line will cause the error

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# This part is just for local testing and won't run in the CI pipeline
if __name__ == '__main__':
    app.run(debug=True)