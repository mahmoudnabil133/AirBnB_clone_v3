#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    "use database storage"
    storage = DBStorage()
    """
    create tables in  database and set up session
    database for (quering, adding objs, del objects)
    """
else:
    from models.engine.file_storage import FileStorage
    "use file storage"
    storage = FileStorage()
    "reload all objects from file"
storage.reload()
