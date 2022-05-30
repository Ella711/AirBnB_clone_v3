#!/usr/bin/python3
from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv

HBNB_API_HOST = getenv('HBNB_API_HOST')
HBNB_API_PORT = getenv('HBNB_API_PORT')

app = Flask(__name__)
app.register_blueprint(app_views)


def port_host(HBNB_API_HOST, HBNB_API_PORT):
    if not HBNB_API_HOST:
        HBNB_API_HOST = '0.0.0.0'
    if not HBNB_API_PORT:
        HBNB_API_PORT = '5000'


@app.teardown_appcontext
def teardown(exception):
    """ handle app teardowns with storage close """
    storage.close()


if __name__ == "__main__":
    port_host(HBNB_API_HOST, HBNB_API_PORT)
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, debug=True, threaded=True)
