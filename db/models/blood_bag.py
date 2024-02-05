#!/usr/bin/python3
"""BloodBag Model"""
from db.models.base import BaseModel, Base
from sqlalchemy import (Column, CheckConstraint, Enum,
                        Integer, ForeignKey, String)


class BloodBag(BaseModel, Base):
    """Class for blood_bags table"""
    __tablename__ = 'blood_bags'

    blood_category = Column(Enum('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-',
                                 'O+', 'O-'), nullable=False)
    quantity = Column(Integer,
                      nullable=False)
    situation = Column(Enum('Stable', 'Soon Shortage', 'Critic'),
                       nullable=False)
    center_id = Column(Integer, ForeignKey('transfusion_centers.id'),
                       nullable=False)

    def __repr__(self):
        """String representation of a BloodBag instance"""
        from db import storage

        string = super().__repr__()
        TC = storage.get('TC', self.center_id)
        string += f'\n\t({self.blood_category}) Blood Bag from {TC.name} TC '
        string += f'({self.quantity} bags / {self.situation} situation)'
        return string
