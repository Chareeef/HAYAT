#!/usr/bin/python3
"""Unittest module to ensure proper working of our storage"""
from datetime import datetime
from db.storage import Storage
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter
from db.models.donor import Donor
from db.models.blood_bag import BloodBag
from db.models.donors_centers import donors_centers
import unittest


class TestStorageInstance(unittest.TestCase):
    """Test Storage Instance globally"""

    @classmethod
    def setUpClass(cls):
        """Runs at class beginning"""
        cls.storage = Storage()
        cls.storage.load_all()

    def test_type(self):
        """Test storage type"""
        self.assertIs(type(self.storage), Storage)

    def test_empty(self):
        """Verify that storage is empty"""
        self.assertEqual(self.storage.all('Country'), [])
        self.assertEqual(self.storage.all('City'), [])
        self.assertEqual(self.storage.all('TransfusionCenter'), [])
        self.assertEqual(self.storage.all('TC'), [])
        self.assertEqual(self.storage.all('Donor'), [])
        self.assertEqual(self.storage.all('BloodBag'), [])
        self.assertEqual(self.storage.all(), [])
