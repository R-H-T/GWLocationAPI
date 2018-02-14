# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from sqlalchemy import Column, String, Integer
from passlib.apps import custom_app_context as password_context
from sqlalchemy.orm import relationship

from model.database import Base
from model.validators import TypeValidator


class User(Base):
    """The User"""
    __tablename__ = 'user'

    # COLUMNS
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False, index=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    display_name = Column(String(64), nullable=False)
    password_hash = Column(String(64), nullable=False)
    birth_date = Column(Integer, nullable=True)
    signup_date = Column(Integer, nullable=False)

    # RELATIONSHIP
    locations = relationship('Location', backref='user', cascade='all, delete, delete-orphan')

    # INITIALIZERS
    def __init__(self,
                 first_name,
                 last_name,
                 display_name,
                 email,
                 locations=None):

        # Check types – TODO: Can be removed later, this is just for demonstrating unit tests.
        TypeValidator.check_string(first_name, 'first_name')
        TypeValidator.check_string(last_name, 'last_name')
        TypeValidator.check_string(display_name, 'display_name')
        TypeValidator.check_string(email, 'email')
        TypeValidator.check_list(locations, 'locations')

        # Assign values
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.email = email

        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

    @property
    def full_name(self):
        """Gets the full name"""

        first_name = self.first_name
        last_name = self.last_name

        if first_name and last_name is not None and not "":
            return "{} {}".format(first_name, last_name)
        elif (first_name is not None or not "") and (last_name is None or ""):
            return first_name
        elif (first_name is None or "") and (last_name is not None or not ""):
            return last_name
        elif first_name and last_name is None or "":
            return None

    @property
    def locations_count(self):
        """Returns the count of the user's locations"""
        return len(self.locations)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'display_name': self.display_name,
            'password_hash': self.password_hash,
            'birth_date': self.birth_date,
            'signup_date': self.signup_date
        }

    def add_location(self, location):
        """Add a new location to the user's location list."""
        self.locations.append(location)
        success = location in self.locations  # Defining success.
        return success

    def hash_password(self, password):
        self.password_hash = password_context.encrypt(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password_hash)

