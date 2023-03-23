#!/usr/bin/python3
""" Module for testing db storage"""
import models
import unittest
import os
from models import storage
from models.user import User
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


@unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
class TestDBStorage(unittest.TestCase):
    """Tests the DBStorage class"""

    def setUp(cls):
        '''
            Sets up the environment for testing DBStorage
        '''
        """Setup the class"""
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = "Betty@mail.com"
        cls.user.password = "hbtndev"
        cls.storage = DBStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        pass

    def test_all(self):
        """Tests all method"""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 6)

    def test_new(self):
        """Tests new method"""
        obj = storage.all()
        user = User()
        user.id = 123455
        user.first_name = "Liam"
        user.last_name = "Stone"
        user.email = "liamstone@gmail.com"
        user.password = "sdf55"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        if os.environ['HBNB_TYPE_STORAGE'] != 'db':
            self.assertIsNotNone(obj[key])

    def test_save(self):
        """Test save method."""
        storage = DBStorage()
        st = State(name="California")
        self.storage.new(st)
        store = list(self.storage._DBStorage__session.new)
        self.assertIn(st, store)

    def test_delete(self):
        """ Tests delete method
        """
        storage = DBStorage()
        st = State(name="New_York")
        self.storage.__session.add(st)
        self.storage.__session.commit()
        self.storage.delete(st)
        self.assertIn(st, list(self.storage._DBStorage__session.deleted))

    def test_reload_DBStorage(self):
        """
        Tests reload method
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        x = self.storage._DBStorage__session
        self.storage.reload()
        y = self.storage._DBStorage__session
        self.assertNotEqual(x, y)


if __name__ == "__main__":
    unittest.main()
