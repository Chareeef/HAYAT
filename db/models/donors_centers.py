#!/usr/bin/python3
"""Association table between donors and transfusion_centers"""
from db.models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, Table

donors_centers = Table('donors_centers', Base.metadata,
                       Column('center_id', Integer,
                              ForeignKey('transfusion_centers.id',
                                         ondelete='CASCADE')),
                       Column('donor_id', Integer,
                              ForeignKey('donors.id',
                                         ondelete='CASCADE')))
