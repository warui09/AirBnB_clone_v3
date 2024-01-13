#!/usr/bin/python3
"""starts a flask app"""

from api.v1.views import app_views
from flask import Flask
from models import storage
import os

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def app_teardown:
    storage.close()


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    threaded = True

    app.run(host=host, port=port, threaded=threaded)
