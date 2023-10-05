#!/usr/bin/python3
"""__init__ magic method for models directory"""
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
