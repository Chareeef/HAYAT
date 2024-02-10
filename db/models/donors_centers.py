#!/usr/bin/python3
"""Association table between donors and transfusion_centers"""
from db.models.base import Base
from sqlalchemy import Column, ForeignKey, String, Table

donors_centers = Table('donors_centers', Base.metadata,
                       Column('center_id', String(50),
                              ForeignKey('transfusion_centers.id',
                                         ondelete='CASCADE')),
                       Column('donor_id', String(50),
                              ForeignKey('donors.id',
                                         ondelete='CASCADE')))
