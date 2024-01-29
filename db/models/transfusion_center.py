#!/usr/bin/python3
"""Transfusion Center Model"""
from db.models.base import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String


class TransfusionCenter(BaseModel, Base):
    """Class for transfusion_enters table"""
    __tablename__ = 'transfusion_centers'

    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(50), nullable=False, unique=True)
    coordinates = Column(String(50))
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
