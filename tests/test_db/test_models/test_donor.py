#!/usr/bin/python3
"""Unittest module to check that Donor Model works as expected"""
from datetime import datetime
from db.models.base import Base, BaseModel
from db.models.donor import Donor
from sqlalchemy.exc import IntegrityError
import unittest


class TestDonor(unittest.TestCase):
    """Test Donor Model"""

    @classmethod
    def setUpClass(cls):
        """Runs at class beginning to create tables and sqlalchemy session"""
        from db import storage

        Base.metadata.drop_all(bind=storage._Storage__engine)
        storage.load_all()

        cls.storage = storage

        cls.joe = Donor(username='joe79',
                        email='joe@ex.com', password_hash='joe-hash-965',
                        phone_number='0600117708',
                        full_name='Joe Doe', age=32,
                        gender='Male', blood_category='O-')
        cls.jane = Donor(username='jane94',
                         email='jane@ex.com', password_hash='jane-hash-645',
                         full_name='Jane Doe', age=24,
                         gender='Female')

        cls.jane.save()
        cls.joe.save()

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_donor_type(self):
        """Test Donor object type"""
        self.assertIs(type(self.jane), Donor)
        self.assertTrue(issubclass(Donor, BaseModel))
        self.assertTrue(issubclass(Donor, Base))

    def test_donor_attributes(self):
        """Test donor instances attributes"""

        self.assertEqual(self.jane.username, 'jane94')
        self.assertEqual(self.joe.username, 'joe79')

        self.assertEqual(self.jane.password_hash, 'jane-hash-645')
        self.assertEqual(self.joe.password_hash, 'joe-hash-965')

        self.assertEqual(self.jane.email, 'jane@ex.com')
        self.assertEqual(self.joe.email, 'joe@ex.com')

        self.assertEqual(self.jane.full_name, 'Jane Doe')
        self.assertEqual(self.joe.full_name, 'Joe Doe')

        self.assertEqual(self.jane.age, 24)
        self.assertEqual(self.joe.age, 32)

        self.assertEqual(self.jane.gender, 'Female')
        self.assertEqual(self.joe.gender, 'Male')

        self.assertEqual(self.joe.phone_number, '0600117708')
        self.assertEqual(self.joe.blood_category, 'O-')

        self.assertIs(type(self.jane.created_at), datetime)
        self.assertIs(type(self.jane.updated_at), datetime)

    def test_missing_attributes(self):
        """Check Integrity Error"""
        error_donor = Donor(username='jane94',
                            email='jane@ex.com', password_hash='jane-hash-645',
                            gender='Female')

        with self.assertRaises(IntegrityError):
            error_donor.save()
