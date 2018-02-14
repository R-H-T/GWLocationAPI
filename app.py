# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from model import User
from flask import Flask, jsonify, request, g
from flask_httpauth import HTTPBasicAuth
from model.database import DatabaseManager

# ENCODING
import sys
import codecs

from controller import IndexController, FindController, LocationsController

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getreader('utf8')(sys.stderr)

# APP
app = Flask(__name__)
app.config.from_object('config')

# Template
app.jinja_env.globals['app_title'] = 'GW\'s Location API'

# Navigation
link_home = dict(title='Home', href='./')
link_find_location = dict(title='Find location', href='./find/')
app.jinja_env.globals['home_links'] = [link_home, link_find_location]

# DATABASE
DatabaseManager()

# Security
auth = HTTPBasicAuth()


# INDEX

@auth.verify_password
def verify_password(email, password):
    user = DatabaseManager.session.query(User).filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.route('/', methods=['GET'])
def index():
    """Main Page"""
    index_controller = IndexController('Welcome to GW Locations!')
    content = """
              This is a RESTful API demo written by {author}.<br />
              Follow the instructions in the README found within this project's directory. <br />
              """.format(author=__author__)
    index_controller.add_to_args({'content': content})
    return index_controller.render_view()


# FIND LOCATION

@app.route('/find/<location>', methods=['GET'])
def find(location):
    """Find a location returns a JSON of found results"""
    find_controller = FindController()
    locations = find_controller.search_location(location)
    status = 'OK'
    if len(locations) is 0:
        status = 'ZERO_RESULTS'
    return jsonify(results=[i.serialize_excluding_id for i in locations], status=status)


# LOCATIONS

@app.route('/locations', methods=['GET'])
@app.route('/locations/', methods=['GET'])
def get_all_locations():
    locations_controller = LocationsController()
    locations = locations_controller.get_all()
    return jsonify(results=[i.serialize for i in locations], status='ZERO_RESULTS')


@app.route('/locations', methods=['POST'])
@app.route('/locations/', methods=['POST'])
@auth.login_required
def create_location():
    name = request.args.get('name', '')
    latitude = request.args.get('latitude', '')
    longitude = request.args.get('longitude', '')
    locations_controller = LocationsController()
    success = locations_controller.create_location(name=name,
                                                   latitude=latitude,
                                                   longitude=longitude)
    if success:
        result = "Object created."
        status = "OK"
    else:
        result = "Feature not yet configured."
        status = "TODO"
    return jsonify(result=result, status=status)


@app.route("/locations/<int:_id>", methods=['GET'])
def get_location_by_id(_id):
    method = request.method
    # get by id
    if method == 'GET':
        return 'Searching for location with id %s' % _id


@app.route("/locations/<int:_id>", methods=['PUT', 'DELETE'])
@auth.login_required
def location_by_id(_id):
    method = request.method
    # update
    if method == 'PUT':
        return 'Updating item #%s if authorized...' % _id
    # delete
    elif method == 'DELETE':
        return 'Deleting item #%s...' % _id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
