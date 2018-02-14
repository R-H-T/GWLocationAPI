# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

import sys
import unittest

sys.path.append('.')

from model import User, Location


class TestUser(unittest.TestCase):

    def setUp(self):
        self.first_name = "John"
        self.last_name = "Appleseed"
        self.display_name = "Johnny"
        self.email = "john.appleseed@example.com"
        self.locations = []

        self.sut = User(first_name=self.first_name,
                        last_name=self.last_name,
                        display_name=self.display_name,
                        email=self.email,
                        locations=self.locations)

    def tearDown(self):
        self.sut = None

    def test_init(self):
        """Should return a successfully initialized User-instance with given parameters."""
        self.assertIsNotNone(self.sut)

        self.assertEqual(self.sut.first_name, self.first_name)
        self.assertEqual(self.sut.last_name, self.last_name)
        self.assertEqual(self.sut.display_name, self.display_name)
        self.assertEqual(self.sut.email, self.email)
        self.assertEqual(self.sut.locations, self.locations)

        self.assertNotEqual(self.sut.first_name, None)
        self.assertNotEqual(self.sut.last_name, None)
        self.assertNotEqual(self.sut.display_name, None)
        self.assertNotEqual(self.sut.email, None)
        self.assertNotEqual(self.sut.locations, None)

        self.assertNotEqual(self.sut.first_name, 0)
        self.assertNotEqual(self.sut.last_name, 0)
        self.assertNotEqual(self.sut.display_name, 0)
        self.assertNotEqual(self.sut.email, 0)
        self.assertNotEqual(self.sut.locations, 0)

    def test_init_types(self):
        """Should raise `TypeError` if non-intended types are given as arguments."""
        # first_name
        self.assertRaises(TypeError,
                          User.__init__,
                          first_name=123,
                          last_name=self.last_name,
                          display_name=self.display_name,
                          email=self.email,
                          locations=self.locations)
        # last_name
        self.assertRaises(TypeError,
                          User.__init__,
                          first_name=self.first_name,
                          last_name=123,
                          display_name=self.display_name,
                          email=self.email,
                          locations=self.locations)
        # display_name
        self.assertRaises(TypeError,
                          User.__init__,
                          first_name=self.first_name,
                          last_name=self.last_name,
                          display_name=123,
                          email=self.email,
                          locations=self.locations)
        # email
        self.assertRaises(TypeError,
                          User.__init__,
                          first_name=self.first_name,
                          last_name=self.last_name,
                          display_name=self.display_name,
                          email=123,
                          locations=self.locations)
        # locations
        self.assertRaises(TypeError,
                          User.__init__,
                          first_name=self.first_name,
                          last_name=self.last_name,
                          display_name=self.display_name,
                          email=self.email,
                          locations=123)

    def test_get_full_name(self):
        """Should return the computed attribute `full_name`,
        thus being the User's full name from the available
        name attributes."""

        self.assertIsNotNone(self.sut)

        full_name = "{} {}".format(self.first_name, self.last_name)
        self.assertEqual(self.sut.full_name, full_name)

    def test_locations(self):
        """Should read, and add locations"""
        locations = [
            Location(13.7563309, 100.5017651, 'Bangkok, Thailand'),  # 1
            Location(39.9041999, 116.4073963, 'Beijing, China'),  # 2
            Location(35.6894875, 139.6917064, 'Tokyo, Japan'),  # 3
            Location(37.566535, 126.9779692, 'Seoul, South Korea'),  # 4
            Location(37.7749295, -122.4194155, 'San Francisco, California'),  # 5
            Location(59.32932349999999, 18.0685808, 'Stockholm, Sweden'),  # 6
        ]
        location_japan = Location(35.6894875, 139.6917064, 'Tokyo, Japan')
        location_philippines = Location(14.5995124, 120.9842195, 'Manila, Philippines')  # 7
        self.sut.locations = locations
        self.assertEqual(self.sut.locations_count, 6)
        self.assertEqual(self.sut.locations[2].name, location_japan.name)
        success = self.sut.add_location(location_philippines)
        self.assertTrue(success)
        self.assertEqual(self.sut.locations_count, 7)
        self.assertEqual(self.sut.locations[6], location_philippines)


if __name__ == '__main__':
    unittest.main()
