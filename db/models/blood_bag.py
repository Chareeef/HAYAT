#!/usr/bin/python3
"""BloodBag Model"""
from db.models.base import BaseModel, Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, String


class BloodBag(BaseModel, Base):
    """Class for blood_bags table"""
    __tablename__ = 'blood_bags'

    blood_category = Column(Enum('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-',
                                 'O+', 'O-'), nullable=False)
    quantity = Column(Integer, nullable=False)
    situation = Column(Enum('Stable', 'Soon Shortage', 'Critic'), nullable=False)
    center_id = Column(Integer, ForeignKey('centers.id'), nullable=False)
