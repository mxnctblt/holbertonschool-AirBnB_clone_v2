#!/usr/bin/python3
"""This module defines a class to manage DBStorage for hbnb clone"""
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """class of the storage engine"""
    __engine = None
    __session = None
    __classes = [User, Place, State, City, Amenity, Review]
    def __init__(self):
        """Initialise the DBStorage"""
        user = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        db_env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
        user, passwd, host, database), pool_pre_ping=True)

        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            objects = {}
            for val in self.__session.query(cls).all():
                key = val.__class__.__name__ + '.' + val.id
                objects[key] = val
            return objects
        else:
            classes = self.__classes
            for val in self.__session.query(classes).all():
                key = val.__class__.__name__ + '.' + val.id
                objects[key] = val
            return objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
