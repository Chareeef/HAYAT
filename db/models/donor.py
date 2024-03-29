#!/usr/bin/python3
"""Donor Model"""
from db.models.base import BaseModel, Base
from db.models.donors_centers import donors_centers
from flask_login import UserMixin
import shortuuid
from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship


class Donor(BaseModel, Base, UserMixin):
    """Class for donors table"""
    __tablename__ = 'donors'

    id = Column(String(50), primary_key=True, default=shortuuid.uuid)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(80), nullable=False)
    phone_number = Column(String(20), unique=True)
    full_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum('Male', 'Female'))
    blood_category = Column(Enum('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-',
                                 'O+', 'O-'))
    followed_centers = relationship('TransfusionCenter',
                                    secondary=donors_centers,
                                    back_populates='donors')

    def delete(self):
        """Delete Donor instance"""
        del self.followed_centers
        super().delete()

    def __repr__(self):
        """String representation of a Donor instance"""
        string = super().__repr__()
        string += f'\n\t{self.full_name} ({self.age} years old)'
        if self.followed_centers:
            string += f'\n\tFollowed transfusion centers:\n'
            for center in self.followed_centers:
                string += '\t\t' + center.name + '\n'
        return string
