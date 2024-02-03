#!/usr/bin/python3
"""Unittest module to check that City Model works as expected"""
from datetime import datetime
from db.models.base import Base, BaseModel
from db.models.country import Country
from db.models.city import City
from sqlalchemy.exc import IntegrityError
import unittest


class TestCityInstance(unittest.TestCase):
    """Test City Instance"""

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

        cls.anb = City(name="Annaba", country_id=cls.alg.id)
        cls.err = City(name="Errachidia", country_id=cls.mor.id)
        cls.anb.save()
        cls.err.save()

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_city_type(self):
        """Test City object type"""
        self.assertIs(type(self.err), City)
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, Base))

    def test_city_attributes(self):
        """Test city instances attributes"""
        self.assertEqual(self.anb.id, 1)
        self.assertEqual(self.err.id, 2)

        self.assertEqual(self.anb.name, 'Annaba')
        self.assertEqual(self.err.name, 'Errachidia')

        self.assertEqual(self.anb.country_id, 1)
        self.assertEqual(self.err.country_id, 2)

        self.assertIs(type(self.anb.created_at), datetime)
        self.assertIs(type(self.anb.updated_at), datetime)

    def test_missing_attributes(self):
        """Check Integrity Error"""
        error_city = City(name='error_city')

        with self.assertRaises(IntegrityError):
            error_city.save()
