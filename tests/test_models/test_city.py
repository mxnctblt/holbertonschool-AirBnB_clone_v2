#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "12546"

    def test_state_id(self):
        """ """
        self.assertEqual(type(self.city.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.city.name), str)
