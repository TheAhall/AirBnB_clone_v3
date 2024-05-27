#!/usr/bin/python3
"""
index
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    status route
    :return: response with json
    """
    data = {
        "status": "OK"
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app_views.route('/stats')
def stats():
    """
    Returns the count of all objects by type
    """
    classes = {
        'amenities': storage.count ('Amenity'),
        'cities': storage.count ('City'),
        'places': storage.count ('Place'),
        'reviews': storage.count ('Review'),
        'states': storage.count ('State'),
        'users': storage.count ('User'),
    }
    return jsonify(counts)
