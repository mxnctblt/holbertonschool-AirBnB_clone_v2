#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest
from os import getenv, environ


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_save(self):
        """Tests save method"""
        if environ['HBNB_TYPE_STORAGE'] != 'db':
            self.city.save()
            self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)
