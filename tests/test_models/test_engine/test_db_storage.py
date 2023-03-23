#!/usr/bin/python3
""" Module for testing db storage"""
import models
import unittest
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
        getenv.environ['HBNB_TYPE_STORAGE'] = 'db'
        getenv.environ['HBNB_MYSQL_USER'] = '******'
        getenv.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        getenv.environ['HBNB_MYSQL_HOST'] = 'localhost'
        getenv.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
        self.storage = DBStorage()
        self.my_model = models.BaseModel()
        self.storage.reload()

    def test_DBStorage_type_storage_environ(self):
        '''
            Test if environment is updating
        '''
        self.assertEqual(getenv('HBNB_TYPE_STORAGE'), 'db')

    @classmethod
    def tearDownClass(self):
        """tearDownClass module"""
        self.store._DBStorage__session.close()
        storage.reload()

    def test_all(self):
        """print alls objects"""
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

    def test_new(self):
        """New objects"""
        new_obj = State()
        new_obj.name = "California"
        new_obj.save()
        self.assertTrue(len(self.store.all()), 1)

    def test_save(self):
        """save objects"""
        original_obj = self.storage.all(User)
        self.storage.new(self.user)
        self.storage.save()
        new_obj = self.storage.all(User)
        self.assertTrue(original_obj != new_obj)

    def test_delete(self):
        """ Tests db_storage delete method to delete an object form the db
        """
        original_obj = self.storage.all(User)
        self.storage.new(self.user)
        self.storage.save()
        self.storage.delete(self.user)
        new_obj = self.storage.all(User)
        self.assertTrue(original_obj == new_obj)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_reload(self):
        """Test reload method."""
        og_session = self.storage._DBStorage__session
        self.storage.reload()
        self.assertIsInstance(self.storage._DBStorage__session, Session)
        self.assertNotEqual(og_session, self.storage._DBStorage__session)
        self.storage._DBStorage__session.close()
        self.storage._DBStorage__session = og_session


if __name__ == "__main__":
    unittest.main()