# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

# CONFIGURATION FILE

# MAIN CONFIGURATION
DEBUG = False


class GoogleMapsAPIKeys(object):
    """ Google Maps API Keys """
    # last update: 13 Feb 2018

    # URLs
    BASE_URL = 'https://maps.googleapis.com/maps/api/'

    # Api Key
    API_KEY = 'YOUR_API_KEY_HERE'  # TODO: Add your Google API Key to use Google Maps API

    # Methods
    METHOD_GEOCODE = 'geocode/json?address={address}&key={api_key}'

    # Keys
    STATUS = 'status'
    STATUS_ZERO_RESULTS = 'ZERO_RESULTS'
    RESULTS = 'results'
    GEOMETRY = 'geometry'
    LOCATION = 'location'
    LATITUDE = 'lat'
    LONGITUDE = 'lng'
    ADDRESS_COMPONENTS = 'address_components'
    LONG_NAME = 'long_name'
