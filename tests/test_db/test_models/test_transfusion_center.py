#!/usr/bin/python3
"""Unittest module to check that TransfusionCenter Model works as expected"""
from datetime import datetime
from db.models.base import Base, BaseModel
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter as TC
from sqlalchemy.exc import IntegrityError
import unittest


class TestTransfusionCenter(unittest.TestCase):
    """Test TransfusionCenter Model"""

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

        cls.anb_tc = TC(name="Annaba TC", city_id=cls.anb.id,
                        email="anb_tc@foo.com", password_hash='anb-hash-446',
                        map_coordinates='36° 54′ 15″ North, 7° 45′ 07″ East')
        cls.err_tc = TC(name="Errachidia TC", city_id=cls.err.id,
                        email="err_tc@bar.com", password_hash='err-hash-446')
        cls.anb_tc.save()
        cls.err_tc.save()

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_TC_type(self):
        """Test TransfusionCenter object type"""
        self.assertIs(type(self.err_tc), TC)
        self.assertTrue(issubclass(TC, BaseModel))
        self.assertTrue(issubclass(TC, Base))

    def test_TC_attributes(self):
        """Test TransfusionCenter instances attributes"""
        self.assertEqual(self.anb_tc.name, 'Annaba TC')
        self.assertEqual(self.err_tc.name, 'Errachidia TC')

        self.assertEqual(self.anb_tc.city_id, 1)
        self.assertEqual(self.err_tc.city_id, 2)

        self.assertEqual(self.anb_tc.map_coordinates,
                         '36° 54′ 15″ North, 7° 45′ 07″ East')

        self.assertIs(type(self.anb_tc.created_at), datetime)
        self.assertIs(type(self.anb_tc.updated_at), datetime)

    def test_missing_attributes(self):
        """Check Integrity Error"""
        error_tc = TC(name='error_tc')

        with self.assertRaises(IntegrityError):
            error_tc.save()
