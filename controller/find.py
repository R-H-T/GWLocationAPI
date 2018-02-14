# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from model import Location
from model.clients.google.maps_cli import get_geocode_location


class FindController:
    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def search_location(self, location):
        try:
            latitude, longitude, name = get_geocode_location(location)
            if latitude is not None and longitude is not None:
                location = Location(name, latitude, longitude)
                self.add_result(location)
                return self.results
        except:  # TODO: Handle more exceptions.
            pass
        return []
