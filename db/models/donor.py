#!/usr/bin/python3
"""Donor Model"""
from db.models.base import BaseModel, Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, String


class Donor(BaseModel, Base):
    """Class for donors table"""
    __tablename__ = 'donors'

    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(50), nullable=False)
    full_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum('Male', 'Female'))
    blood_ = Column(Enum('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
