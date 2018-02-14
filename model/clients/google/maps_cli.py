# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

import httplib2
import json

# Encoding
import sys
import codecs

from config import GoogleMapsAPIKeys

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getreader('utf8')(sys.stderr)


# Methods
def get_geocode_location(input_string):
    location_string = input_string.replace(' ', '+')
    keys = GoogleMapsAPIKeys
    method = keys.METHOD_GEOCODE.format(address=location_string, api_key=keys.API_KEY)
    url = ('{base_url}{method}'.format(base_url=keys.BASE_URL, method=method))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    data = json.loads(content, encoding='utf-8')
    if keys.STATUS in data and keys.STATUS_ZERO_RESULTS in data[keys.STATUS]:
        raise Exception(keys.STATUS_ZERO_RESULTS)
    first_result = data[keys.RESULTS][0]
    name = first_result[keys.ADDRESS_COMPONENTS][0][keys.LONG_NAME]
    location = first_result[keys.GEOMETRY][keys.LOCATION]
    latitude = location[keys.LATITUDE]
    longitude = location[keys.LONGITUDE]
    return latitude, longitude, name
