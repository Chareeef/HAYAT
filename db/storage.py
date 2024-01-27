#!/usr/bin/python3
"""This module set the basement of our project database"""
from db.base import Base
# import db.models
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

    def load_all(self):
        """Create tables and sqlalchemy session"""
        Base.metadata.create_all(self.__engine)

        session_factory = scoped_session(sessionmaker(bind=self.__engine))
        self.__session = session_factory()
