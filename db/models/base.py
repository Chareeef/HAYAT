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

    def __init__(self, **kwargs):
        """Initialize our models"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """String representation of the object"""
        string = f'{self.__class__.__name__} : name -> {self.name} '
        string += f'(created at {self.created_at})'
        return string
