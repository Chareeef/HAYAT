#!/usr/bin/python3
"""Unittest module to ensure proper working of our storage"""
from datetime import datetime
from db.storage import Storage
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter as TC
from db.models.donor import Donor
from db.models.blood_bag import BloodBag
from db.models.donors_centers import donors_centers
import unittest


class TestStorageInstance(unittest.TestCase):
    """Test Storage Instance globally"""

    @classmethod
    def setUpClass(cls):
        """Runs at class beginning to create tables and sqlalchemy session"""
        cls.storage = Storage()
        cls.storage.load_all()

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

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


class TestStorageAll(unittest.TestCase):
    """Test Storage all method"""

    @classmethod
    def setUpClass(cls):
        """Runs at class beginning to create tables,
        sqlalchemy session and some sample data
        """
        storage = Storage()
        storage.load_all()

        cls.mor = Country(name='Morrocco')
        cls.chili = Country(name='Chili')
        storage.add_all([cls.mor, cls.chili])
        storage.commit()

        cls.err = City(name='Errachidia', country_id=cls.mor.id)
        storage.add(cls.err)
        storage.commit()

        cls.sah = TC(name='Sahraoui',
                     email='sah@ex.com', password_hash='nkmjuh',
                     phone_number='0334129876', city_id=cls.err.id)
        storage.add(cls.sah)
        storage.commit()

        cls.ych = Donor(username='youcha',
                        email='ych@ex.com', password_hash='poulkll',
                        phone_number='0607798008',
                        full_name='Youssef Charif', age=21,
                        gender='Male', blood_category='O-')
        storage.add(cls.ych)
        storage.commit()

        cls.bag = BloodBag(blood_category='O-', quantity=6, situation='Critic',
                           center_id=cls.sah.id)
        storage.add(cls.bag)
        storage.commit()

        cls.storage = storage

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_all_objects(self):
        """Test all() method without parameter"""
        all_dict = self.storage.all()

        self.assertEqual(len(all_dict), 6)
        self.assertIn(self.mor, all_dict)
        self.assertIn(self.chili, all_dict)
        self.assertIn(self.err, all_dict)
        self.assertIn(self.ych, all_dict)
        self.assertIn(self.sah, all_dict)
        self.assertIn(self.bag, all_dict)

    def test_with_country(self):
        """Test all() method with 'Country'"""
        country_dict = self.storage.all('Country')

        self.assertEqual(len(country_dict), 2)
        self.assertIn(self.mor, country_dict)
        self.assertIn(self.chili, country_dict)
        self.assertNotIn(self.err, country_dict)
        self.assertNotIn(self.ych, country_dict)
        self.assertNotIn(self.sah, country_dict)
        self.assertNotIn(self.bag, country_dict)

    def test_with_city(self):
        """Test all() method with 'City'"""
        city_dict = self.storage.all('City')

        self.assertEqual(len(city_dict), 1)
        self.assertNotIn(self.mor, city_dict)
        self.assertNotIn(self.chili, city_dict)
        self.assertIn(self.err, city_dict)
        self.assertNotIn(self.ych, city_dict)
        self.assertNotIn(self.sah, city_dict)
        self.assertNotIn(self.bag, city_dict)

    def test_with_donor(self):
        """Test all() method with 'Donor'"""
        donor_dict = self.storage.all('Donor')

        self.assertEqual(len(donor_dict), 1)
        self.assertNotIn(self.mor, donor_dict)
        self.assertNotIn(self.chili, donor_dict)
        self.assertNotIn(self.err, donor_dict)
        self.assertIn(self.ych, donor_dict)
        self.assertNotIn(self.sah, donor_dict)
        self.assertNotIn(self.bag, donor_dict)

    def test_with_transfusion_center(self):
        """Test all() method with 'TransfusionCenter'"""
        center_dict = self.storage.all('TransfusionCenter')

        self.assertEqual(len(center_dict), 1)
        self.assertNotIn(self.mor, center_dict)
        self.assertNotIn(self.chili, center_dict)
        self.assertNotIn(self.err, center_dict)
        self.assertNotIn(self.ych, center_dict)
        self.assertIn(self.sah, center_dict)
        self.assertNotIn(self.bag, center_dict)

        tc_dict = self.storage.all('TC')

        self.assertEqual(len(tc_dict), 1)
        self.assertIn(self.sah, tc_dict)

    def test_with_blood_bag(self):
        """Test all() method with 'BloodBag'"""
        bag_dict = self.storage.all('BloodBag')

        self.assertEqual(len(bag_dict), 1)
        self.assertNotIn(self.mor, bag_dict)
        self.assertNotIn(self.chili, bag_dict)
        self.assertNotIn(self.err, bag_dict)
        self.assertNotIn(self.ych, bag_dict)
        self.assertNotIn(self.sah, bag_dict)
        self.assertIn(self.bag, bag_dict)
