#!/usr/bin/python3
""" Module for testing db storage"""
import models
import unittest
import os
from os import getenv
from models import storage
from models.user import User
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm.session import Session


class TestDBStorage(unittest.TestCase):
    """Tests the DBStorage class"""

    def setUp(self):
        '''
            Sets up the environment for testing DBStorage
        '''
        """Setup the class"""
        self.user = User()
        self.user.first_name = "Betty"
        self.user.last_name = "Holberton"
        self.user.email = "Betty@mail.com"
        self.user.password = "hbtndev"
        self.storage = DBStorage()
        self.storage.reload()

    def test_DBStorage_type_storage_environ(self):
        '''
            Test if environment is updating
        '''
        self.assertEqual(getenv('HBNB_TYPE_STORAGE'), 'db')

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        pass

    def test_all(self):
        """Tests all method"""
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

    def test_new(self):
        """Tests new method"""
        new_obj = State()
        new_obj.name = "California"
        new_obj.save()
        self.assertTrue(len(self.store.all()), 1)

    def test_save(self):
        """Tests save method"""
        original_obj = self.storage.all(User)
        self.storage.new(self.user)
        self.storage.save()
        new_obj = self.storage.all(User)
        self.assertTrue(original_obj != new_obj)

    def test_delete(self):
        """ Tests delete method
        """
        st = State(name="New_York")
        self.storage._DBStorage__session.add(st)
        self.storage._DBStorage__session.commit()
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
