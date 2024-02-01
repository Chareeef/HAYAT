#!/usr/bin/python3
"""City Model"""
from db.models.base import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Class for cities table"""
    __tablename__ = 'cities'

    name = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    centers = relationship('TransfusionCenter', backref='city',
                           cascade='all, delete-orphan')
