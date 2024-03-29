#!/usr/bin/python3
"""good file to doc"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.user import User


class DBStorage:
    "class represent database storage"
    __engine = None
    __session = None

    def __init__(self):
        "init method for instances"
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB
            ), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "return all inctances for class"
        if not cls:
            rows = []
            class_lists = [User, Place, City, State, Amenity, Review]
            for cls in class_lists:
                temp = self.__session.query(cls).all()
                rows += temp
        else:
            rows = self.__session.query(cls).all()
        dec = {}
        for r in rows:
            key = '{}.{}'.format(r.__class__.__name__, r.id)
            dec[key] = r
        return dec

    def new(self, obj):
        "add new object to database"
        self.__session.add(obj)

    def save(self):
        "save changes"
        self.__session.commit()

    def save_all(self, lis):
        self.__session.add_all(lis)
        self.__session.commit()

    def delete(self, obj=None):
        "delete object from database"
        if obj:
            self.__session.delete(obj)

    def reload(self):
        "create tables and setup __session atr"
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Sess = scoped_session(Session)
        self.__session = Sess

    def close(self):
        "close doc"
        self.__session.remove()

    def get(self, cls, id):
        """gets an object"""
        obj = models.storage.all(cls)
        for i, j in obj.items():
            match = cls + '.' + id
            if i == match:
                return j
        return None

    def count(self, cls=None):
        """count no. of objects"""
        obj = models.storage.all(cls)
        return len(obj)
