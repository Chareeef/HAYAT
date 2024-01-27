#!/usr/bin/python3
"""This module set the basement of our project database"""
from db.models import classes_dict
from db.models.base import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Storage():
    """Our database manager class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize storage"""
        user = getenv('HAYAT_USER')
        password = getenv('HAYAT_PWD')
        host = getenv('HAYAT_HOST')
        database = getenv('HAYAT_DB')

        db_url = f'mysql+mysqldb://{user}:{password}@{host}/{database}'
        self.__engine = create_engine(db_url)

        if database == 'hayat_test_db':
            Base.metadata.drop_all(bind=self.__engine)

    def load_all(self):
        """Create tables and sqlalchemy session"""
        Base.metadata.create_all(self.__engine)

        session_factory = scoped_session(sessionmaker(bind=self.__engine))
        self.__session = session_factory()

    def all(self, obj_name=None):
        """Retrieve all database records"""
        session = self.__session

        if obj_name:
            obj = classes_dict[obj_name]
            return session.query(obj).all()
        else:
            objs_list = []
            for obj in classes_dict.values():
                objs_list += session.query(obj).all()
            return objs_list

    def add(self, obj):
        """Add an object to the database"""
        self.__session.add(obj)

    def add_all(self, objs):
        """Add a list of objects to the database"""
        self.__session.add_all(objs)

    def delete(self, obj):
        """Delete an object from the database"""
        self.__session.delete(obj)

    def commit(self):
        """Commit a transaction to the database"""
        self.__session.commit()
