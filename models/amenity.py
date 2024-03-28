#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """amenity class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
