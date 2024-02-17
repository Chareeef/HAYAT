#!/usr/bin/python3
"""Transfusion Center Model"""
from db.models.base import BaseModel, Base
from db.models.donors_centers import donors_centers
from flask_login import UserMixin
import shortuuid
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class TransfusionCenter(BaseModel, Base, UserMixin):
    """Class for transfusion_enters table"""
    __tablename__ = 'transfusion_centers'

    id = Column(String(50), primary_key=True, default=shortuuid.uuid)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(80), nullable=False)
    phone_number = Column(String(20), unique=True)
    location = Column(String(80))
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    blood_bags = relationship('BloodBag', backref='center',
                              cascade='all, delete-orphan')
    donors = relationship('Donor', secondary=donors_centers,
                          back_populates='followed_centers')

    def delete(self):
        """Delete TransfusionCenter instance"""
        del self.donors
        super().delete()
