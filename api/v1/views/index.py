#!/usr/bin/python3
""" index module for viewing request status  """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ view status """
    return jsonify({"status": "OK"})
