#!/usr/bin/python3
"""Our base models"""
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel():
    """The base model of our database tables"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow())
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow(),
                        onupdate=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize our models"""
        if not kwargs:
            print('It is better to pass a dictionnary')
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']

        return obj_dict

    def __repr__(self):
        """String representation of the object"""
        string = f'{self.__class__.__name__} : name -> {self.name} '
        string += f'(created at {self.created_at})'
        return string
