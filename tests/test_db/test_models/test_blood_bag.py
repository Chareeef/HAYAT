#!/usr/bin/python3
"""Unittest module to check that BloodBag Model works as expected"""
from datetime import datetime
from db.models.base import Base, BaseModel
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter as TC
from db.models.blood_bag import BloodBag
from sqlalchemy.exc import IntegrityError
import unittest


class TestBloodBag(unittest.TestCase):
    """Test BloodBag Model"""

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

        cls.anb = City(name='Annaba', country_id=cls.alg.id)
        cls.err = City(name='Errachidia', country_id=cls.mor.id)
        cls.anb.save()
        cls.err.save()

        cls.anb_tc = TC(name='Annaba TC', city_id=cls.anb.id,
                        email='anb_tc@foo.com', password_hash='anb-hash-446')
        cls.err_tc = TC(name='Errachidia TC', city_id=cls.err.id,
                        email='err_tc@bar.com', password_hash='err-hash-446')
        cls.anb_tc.save()
        cls.err_tc.save()

        cls.anb_tc_bag_ab = BloodBag(blood_category='AB+',
                                     quantity=27,
                                     situation='Stable',
                                     center_id=cls.anb_tc.id)

        cls.anb_tc_bag_o = BloodBag(blood_category='O-',
                                    quantity=14,
                                    situation='Soon Shortage',
                                    center_id=cls.anb_tc.id)

        cls.err_tc_bag_ab = BloodBag(blood_category='AB-',
                                     quantity=9,
                                     situation='Critic',
                                     center_id=cls.err_tc.id)

        cls.err_tc_bag_a = BloodBag(blood_category='A+',
                                    quantity=30,
                                    situation='Stable',
                                    center_id=cls.err_tc.id)

        cls.anb_tc_bag_ab.save()
        cls.anb_tc_bag_o.save()
        cls.err_tc_bag_ab.save()
        cls.err_tc_bag_a.save()

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_BloodBag_type(self):
        """Test BloodBag object type"""
        self.assertIs(type(self.anb_tc_bag_ab), BloodBag)
        self.assertTrue(issubclass(BloodBag, BaseModel))
        self.assertTrue(issubclass(BloodBag, Base))

    def test_BloodBag_attributes(self):
        """Test BloodBag instances attributes"""
        self.assertEqual(self.anb_tc_bag_ab.id, 1)
        self.assertEqual(self.anb_tc_bag_o.id, 2)
        self.assertEqual(self.err_tc_bag_ab.id, 3)
        self.assertEqual(self.err_tc_bag_a.id, 4)

        self.assertEqual(self.anb_tc_bag_ab.blood_category, 'AB+')
        self.assertEqual(self.anb_tc_bag_o.blood_category, 'O-')
        self.assertEqual(self.err_tc_bag_ab.blood_category, 'AB-')
        self.assertEqual(self.err_tc_bag_a.blood_category, 'A+')

        self.assertEqual(self.anb_tc_bag_ab.quantity, 27)
        self.assertEqual(self.anb_tc_bag_o.quantity, 14)
        self.assertEqual(self.err_tc_bag_ab.quantity, 9)
        self.assertEqual(self.err_tc_bag_a.quantity, 30)

        self.assertEqual(self.anb_tc_bag_ab.situation, 'Stable')
        self.assertEqual(self.anb_tc_bag_o.situation, 'Soon Shortage')
        self.assertEqual(self.err_tc_bag_ab.situation, 'Critic')
        self.assertEqual(self.err_tc_bag_a.situation, 'Stable')

        self.assertEqual(self.anb_tc_bag_ab.center_id, self.anb_tc.id)
        self.assertEqual(self.anb_tc_bag_o.center_id, self.anb_tc.id)
        self.assertEqual(self.err_tc_bag_ab.center_id, self.err_tc.id)
        self.assertEqual(self.err_tc_bag_a.center_id, self.err_tc.id)

        self.assertIs(type(self.anb_tc.created_at), datetime)
        self.assertIs(type(self.anb_tc.updated_at), datetime)

    def test_missing_attributes(self):
        """Check Integrity Error"""
        error_bag = BloodBag(blood_category='AB-',
                             situation='Critic')

        with self.assertRaises(IntegrityError):
            error_bag.save()
