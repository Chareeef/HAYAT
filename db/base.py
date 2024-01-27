#!/usr/bin/python3
"""Our Databse models"""
from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel():
    """The base model of our database tables"""

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, **kwargs):
        """Initialize our models"""
        for key, val in kwargs.items():
            self.key = val
