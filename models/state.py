#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """
    if (models.storage_t) == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
