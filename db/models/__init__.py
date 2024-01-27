#!/usr/bin/python3
"""Import our models"""
from db.models.country import Country
from db.models.city import City

classes_dict = {
    'Country': Country,
    'City': City
}
