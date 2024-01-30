#!/usr/bin/python3
"""Import our models"""
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter
from db.models.donor import Donor
from db.models.blood_bag import BloodBag

classes_dict = {
    'Country': Country,
    'City': City,
    'TransfusionCenter': TransfusionCenter,
    'TC': TransfusionCenter,
    'Donor': Donor,
    'BloodBag': BloodBag
}
