#!/usr/bin/python3
"""Our base models"""
from datetime import datetime
from os import getenv
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel():
    """The base model of our database tables"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow,
            onupdate=datetime.utcnow)

    if getenv('HAYAT_DB') == 'hayat_test_db':
        __counter = 1

    def __init__(self, *args, **kwargs):
        """Initialize our models"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if getenv('HAYAT_DB') == 'hayat_test_db':
            if self.__class__.__name__ == 'BaseModel':
                self.id = BaseModel.__counter
                BaseModel.__counter += 1
                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()

    def save(self):
        """Add and commit the object to the database"""
        from db import storage
        storage.add(self)
        storage.commit()

    def delete(self):
        """Delete the object from the database"""
        from db import storage
        storage.delete(self)
        storage.commit()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()

        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']

        obj_dict['created_at'] = self.created_at.strftime('%Y/%m/%d %H:%M:%S')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y/%m/%d %H:%M:%S')

        return obj_dict

    def __repr__(self):
        """String representation of the object"""
        string = f'{self.__class__.__name__} :\n'

        string += f'\tid = {self.id} -> '

        dictionary = self.to_dict()

        if 'name' in dictionary:
            string += f"name: {dictionary['name']} / "

        string += f"created_at: {dictionary['created_at']} / "
        string += f"updated_at: {dictionary['updated_at']}"

        return string
