#!/usr/bin/python3
"""Transfusion Center Model"""
from db.models.base import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class TransfusionCenter(BaseModel, Base):
    """Class for transfusion_enters table"""
    __tablename__ = 'transfusion_centers'

    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(50), nullable=False)
    coordinates = Column(String(50))
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    blood_bags = relationship('BloodBag', backref='center',
                              cascade='all, delete-orphan')
