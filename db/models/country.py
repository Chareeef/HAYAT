#!/usr/bin/python3
"""Country Model"""
from db.base import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Country(BaseModel, Base):
    """Class for countries table"""
    __tablename__ = 'countries'

    name = Column(String(20), nullable=False, unique=True)
    cities = relationship('City', backref='country',
                          cascade='all, delete-orphan')
