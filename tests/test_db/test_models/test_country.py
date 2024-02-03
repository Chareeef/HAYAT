#!/usr/bin/python3
"""Unittest module to check that Country Model works as expected"""
from datetime import datetime
from db.models.base import Base, BaseModel
from db.models.country import Country
from tests.test_db import fill_database
import unittest


class TestCountryInstance(unittest.TestCase):
    """Test Country Instance"""

    @classmethod
    def setUpClass(cls):
        """Runs at class beginning to create tables and sqlalchemy session"""
        from db import storage

        Base.metadata.drop_all(bind=storage._Storage__engine)
        storage.load_all()

        cls.storage = storage

        cls.alg = Country(name='Algeria')
        cls.mor = Country(name='Morocco')
        cls.alg.save()
        cls.mor.save()

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_country_type(self):
        """Test Country object type"""
        self.assertIs(type(self.alg), Country)
        self.assertTrue(issubclass(Country, BaseModel))
        self.assertTrue(issubclass(Country, Base))

    def test_attributes(self):
        """Test country instances attributes"""
        self.assertEqual(self.alg.id, 1)
        self.assertEqual(self.mor.id, 2)

        self.assertEqual(self.alg.name, 'Algeria')

        self.assertIs(type(self.alg.created_at), datetime)
        self.assertIs(type(self.alg.updated_at), datetime)
