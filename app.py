# app.py

# Triggering the build again for another test.
# The 'requests' import below is what causes the failure.

from flask import Flask
import requets

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)