# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"


class LocationsController:
    """Locations Controller"""

    def __init__(self):
        self.locations = []

    def create_location(self, name, latitude, longitude):
        return False

    def get_location(self, _id):
        pass

    def get_all(self):
        # TODO: Fetch all records
        return []

    def update_location(self, _id):
        pass

    def delete_location(self, _id):
        pass
