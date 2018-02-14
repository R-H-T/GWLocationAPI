# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from sqlalchemy import Column, Integer, String, Float, ForeignKey

from model.database import Base


class Location(Base):
    """ Location """
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))

    def __init__(self, latitude, longitude, name):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    @property
    def serialize(self):
        """Returns the object data in a serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    @property
    def serialize_excluding_id(self):
        """Returns the object data in a serializable format without the `id`-property,"""
        return {
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
