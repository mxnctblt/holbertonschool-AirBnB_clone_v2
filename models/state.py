#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Returns a list of City instances
            with state_id equals to the current State.id
            (FileStorage relationship between State and City)
            """
            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
