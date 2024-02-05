#!/usr/bin/python3
"""Unittest module to check that donors_centers Table works as expected"""
from db.models.base import Base
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter as TC
from db.models.donor import Donor
import unittest


class TestDonorsCenters(unittest.TestCase):
    """Test donors_centers table"""

    def setUp(self):
        """Runs before each test to create tables and sqlalchemy session"""
        from db import storage

        Base.metadata.drop_all(bind=storage._Storage__engine)
        storage.load_all()

        self.storage = storage

        self.alg = Country(name='Algeria')
        self.mor = Country(name='Morocco')
        self.alg.save()
        self.mor.save()

        self.anb = City(name="Annaba", country_id=self.alg.id)
        self.err = City(name="Errachidia", country_id=self.mor.id)
        self.anb.save()
        self.err.save()

        self.anb_tc = TC(name="Annaba TC", city_id=self.anb.id,
                         email="anb_tc@foo.com", password_hash='anb-hash-446')
        self.err_tc = TC(name="Errachidia TC", city_id=self.err.id,
                         email="err_tc@bar.com", password_hash='err-hash-446')
        self.anb_tc.save()
        self.err_tc.save()

        self.joe = Donor(username='joe79',
                         email='joe@ex.com', password_hash='joe-hash-965',
                         full_name='Joe Doe', age=32,
                         gender='Male')
        self.jane = Donor(username='jane94',
                          email='jane@ex.com', password_hash='jane-hash-645',
                          full_name='Jane Doe', age=24,
                          gender='Female')

        self.jane.save()
        self.joe.save()

    def tearDown(self):
        """Runs after each test to close the sqlalchemy session"""
        self.storage.close()

    def test_delete_method(self):
        """Test <Model>.delete() method"""
        ken = Country(name='Kenya')
        ken.save()

        self.assertIn(ken, self.storage.all())
        self.assertIn(self.err_tc, self.storage.all())
        self.assertIn(self.anb_tc, self.storage.all())
        self.assertIn(self.jane, self.storage.all())
        self.assertIn(self.joe, self.storage.all())

        ken.delete()
        self.err_tc.delete()
        self.anb_tc.delete()
        self.jane.delete()
        self.joe.delete()

        self.assertNotIn(ken, self.storage.all())
        self.assertNotIn(self.err_tc, self.storage.all())
        self.assertNotIn(self.anb_tc, self.storage.all())
        self.assertNotIn(self.jane, self.storage.all())
        self.assertNotIn(self.joe, self.storage.all())

    def test_no_relationship(self):
        """Test that there are not any donors_centers record yet"""
        self.assertEqual(self.err_tc.donors, [])
        self.assertEqual(self.anb_tc.donors, [])
        self.assertEqual(self.jane.followed_centers, [])
        self.assertEqual(self.joe.followed_centers, [])

    def test_append_donor(self):
        """Test appending a donor to a transfusion center's donors"""
        self.assertNotIn(self.jane, self.err_tc.donors)
        self.assertNotIn(self.joe, self.err_tc.donors)

        self.assertNotIn(self.jane, self.anb_tc.donors)
        self.assertNotIn(self.joe, self.anb_tc.donors)

        self.assertNotIn(self.err_tc, self.jane.followed_centers)
        self.assertNotIn(self.err_tc, self.joe.followed_centers)

        self.assertNotIn(self.anb_tc, self.jane.followed_centers)
        self.assertNotIn(self.anb_tc, self.joe.followed_centers)

        self.err_tc.donors.append(self.jane)
        self.anb_tc.donors.append(self.joe)

        self.assertIn(self.jane, self.err_tc.donors)
        self.assertNotIn(self.joe, self.err_tc.donors)

        self.assertNotIn(self.jane, self.anb_tc.donors)
        self.assertIn(self.joe, self.anb_tc.donors)

        self.assertIn(self.err_tc, self.jane.followed_centers)
        self.assertNotIn(self.err_tc, self.joe.followed_centers)

        self.assertNotIn(self.anb_tc, self.jane.followed_centers)
        self.assertIn(self.anb_tc, self.joe.followed_centers)

    def test_append_TC(self):
        """Test appending a transfusion center to a donor's followed_centers"""
        self.assertNotIn(self.jane, self.err_tc.donors)
        self.assertNotIn(self.joe, self.err_tc.donors)

        self.assertNotIn(self.jane, self.anb_tc.donors)
        self.assertNotIn(self.joe, self.anb_tc.donors)

        self.assertNotIn(self.err_tc, self.jane.followed_centers)
        self.assertNotIn(self.err_tc, self.joe.followed_centers)

        self.assertNotIn(self.anb_tc, self.jane.followed_centers)
        self.assertNotIn(self.anb_tc, self.joe.followed_centers)

        self.jane.followed_centers.append(self.err_tc)
        self.joe.followed_centers.append(self.anb_tc)

        self.assertIn(self.jane, self.err_tc.donors)
        self.assertNotIn(self.joe, self.err_tc.donors)

        self.assertNotIn(self.jane, self.anb_tc.donors)
        self.assertIn(self.joe, self.anb_tc.donors)

        self.assertIn(self.err_tc, self.jane.followed_centers)
        self.assertNotIn(self.err_tc, self.joe.followed_centers)

        self.assertNotIn(self.anb_tc, self.jane.followed_centers)
        self.assertIn(self.anb_tc, self.joe.followed_centers)

    def test_delete_donors(self):
        """Test cascade effect when deleting donors"""
        self.err_tc.donors.append(self.jane)
        self.err_tc.donors.append(self.joe)

        self.assertIn(self.jane, self.err_tc.donors)
        self.assertIn(self.joe, self.err_tc.donors)
        self.assertIn(self.err_tc, self.jane.followed_centers)
        self.assertIn(self.err_tc, self.joe.followed_centers)

        self.jane.delete()

        self.assertNotIn(self.jane, self.err_tc.donors)
        self.assertIn(self.joe, self.err_tc.donors)
        self.assertNotIn(self.err_tc, self.jane.followed_centers)
        self.assertIn(self.err_tc, self.joe.followed_centers)

        self.joe.delete()

        self.assertNotIn(self.jane, self.err_tc.donors)
        self.assertNotIn(self.joe, self.err_tc.donors)
        self.assertNotIn(self.err_tc, self.jane.followed_centers)
        self.assertNotIn(self.err_tc, self.joe.followed_centers)

    def test_delete_transfusion_centers(self):
        """Test cascade effect when deleting transfusion centers"""
        self.err_tc.donors.append(self.jane)
        self.err_tc.donors.append(self.joe)
        self.anb_tc.donors.append(self.jane)
        self.anb_tc.donors.append(self.joe)

        self.assertIn(self.err_tc, self.jane.followed_centers)
        self.assertIn(self.err_tc, self.joe.followed_centers)
        self.assertIn(self.jane, self.err_tc.donors)
        self.assertIn(self.joe, self.err_tc.donors)

        self.assertIn(self.anb_tc, self.jane.followed_centers)
        self.assertIn(self.anb_tc, self.joe.followed_centers)
        self.assertIn(self.jane, self.anb_tc.donors)
        self.assertIn(self.joe, self.anb_tc.donors)

        self.err_tc.delete()

        self.assertNotIn(self.err_tc, self.jane.followed_centers)
        self.assertNotIn(self.err_tc, self.joe.followed_centers)
        self.assertNotIn(self.jane, self.err_tc.donors)
        self.assertNotIn(self.joe, self.err_tc.donors)

        self.assertIn(self.anb_tc, self.jane.followed_centers)
        self.assertIn(self.anb_tc, self.joe.followed_centers)
        self.assertIn(self.jane, self.anb_tc.donors)
        self.assertIn(self.joe, self.anb_tc.donors)

        self.anb_tc.delete()

        self.assertNotIn(self.err_tc, self.jane.followed_centers)
        self.assertNotIn(self.err_tc, self.joe.followed_centers)
        self.assertNotIn(self.jane, self.err_tc.donors)
        self.assertNotIn(self.joe, self.err_tc.donors)

        self.assertNotIn(self.anb_tc, self.jane.followed_centers)
        self.assertNotIn(self.anb_tc, self.joe.followed_centers)
        self.assertNotIn(self.jane, self.anb_tc.donors)
        self.assertNotIn(self.joe, self.anb_tc.donors)
