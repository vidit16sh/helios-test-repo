# helios-test-repo/app.py

from flask import Flask
from config import FEATURE_FLAG_ENABLED

app = Flask(__name__)

@app.route('/')
def get_feature_status():
    """
    Returns a different message based on the feature flag in config.py.
    """
    if FEATURE_FLAG_ENABLED:
        return "Feature is ON"
    else:
        return "Feature is OFF"

if __name__ == '__main__':
    app.run(debug=True)