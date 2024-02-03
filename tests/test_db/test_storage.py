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


def fill_database(self):
    """Return a ready test storage"""
    storage = Storage()
    storage.load_all()

    self.mor = Country(name='Morrocco')
    self.eth = Country(name='Ethiopia')
    storage.add_all([self.mor, self.eth])
    storage.commit()

    self.err = City(name='Errachidia', country_id=self.mor.id)
    storage.add(self.err)
    storage.commit()

    self.sah = TC(name='Sahraoui',
                  email='sah@ex.com', password_hash='nkmjuh',
                  phone_number='0334129876', city_id=self.err.id)
    storage.add(self.sah)
    storage.commit()

    self.ych = Donor(username='youcha',
                     email='ych@ex.com', password_hash='poulkll',
                     phone_number='0607798008',
                     full_name='Youssef Charif', age=21,
                     gender='Male', blood_category='O-')
    storage.add(self.ych)
    storage.commit()

    self.bag = BloodBag(blood_category='O-', quantity=6, situation='Critic',
                        center_id=self.sah.id)
    storage.add(self.bag)
    storage.commit()

    self.storage = storage


class TestStorageAll(unittest.TestCase):
    """Test Storage all() method"""

    @classmethod
    def setUpClass(cls):
        """Runs at class beginning to create tables,
        sqlalchemy session and some sample data
        """
        fill_database(cls)

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_all_objects(self):
        """Test all() method without parameter"""
        all_dict = self.storage.all()

        self.assertEqual(len(all_dict), 6)
        self.assertIn(self.mor, all_dict)
        self.assertIn(self.eth, all_dict)
        self.assertIn(self.err, all_dict)
        self.assertIn(self.ych, all_dict)
        self.assertIn(self.sah, all_dict)
        self.assertIn(self.bag, all_dict)

    def test_all_with_country(self):
        """Test all() method with 'Country'"""
        country_dict = self.storage.all('Country')

        self.assertEqual(len(country_dict), 2)
        self.assertIn(self.mor, country_dict)
        self.assertIn(self.eth, country_dict)
        self.assertNotIn(self.err, country_dict)
        self.assertNotIn(self.ych, country_dict)
        self.assertNotIn(self.sah, country_dict)
        self.assertNotIn(self.bag, country_dict)

    def test_all_with_city(self):
        """Test all() method with 'City'"""
        city_dict = self.storage.all('City')

        self.assertEqual(len(city_dict), 1)
        self.assertNotIn(self.mor, city_dict)
        self.assertNotIn(self.eth, city_dict)
        self.assertIn(self.err, city_dict)
        self.assertNotIn(self.ych, city_dict)
        self.assertNotIn(self.sah, city_dict)
        self.assertNotIn(self.bag, city_dict)

    def test_all_with_donor(self):
        """Test all() method with 'Donor'"""
        donor_dict = self.storage.all('Donor')

        self.assertEqual(len(donor_dict), 1)
        self.assertNotIn(self.mor, donor_dict)
        self.assertNotIn(self.eth, donor_dict)
        self.assertNotIn(self.err, donor_dict)
        self.assertIn(self.ych, donor_dict)
        self.assertNotIn(self.sah, donor_dict)
        self.assertNotIn(self.bag, donor_dict)

    def test_all_with_transfusion_center(self):
        """Test all() method with 'TransfusionCenter'"""
        center_dict = self.storage.all('TransfusionCenter')

        self.assertEqual(len(center_dict), 1)
        self.assertNotIn(self.mor, center_dict)
        self.assertNotIn(self.eth, center_dict)
        self.assertNotIn(self.err, center_dict)
        self.assertNotIn(self.ych, center_dict)
        self.assertIn(self.sah, center_dict)
        self.assertNotIn(self.bag, center_dict)

        tc_dict = self.storage.all('TC')

        self.assertEqual(len(tc_dict), 1)
        self.assertIn(self.sah, tc_dict)

    def test_all_with_blood_bag(self):
        """Test all() method with 'BloodBag'"""
        bag_dict = self.storage.all('BloodBag')

        self.assertEqual(len(bag_dict), 1)
        self.assertNotIn(self.mor, bag_dict)
        self.assertNotIn(self.eth, bag_dict)
        self.assertNotIn(self.err, bag_dict)
        self.assertNotIn(self.ych, bag_dict)
        self.assertNotIn(self.sah, bag_dict)
        self.assertIn(self.bag, bag_dict)


class TestStorageAddCommit(unittest.TestCase):
    """Test Storage add(), add_all(), and commit() methods"""

    def setUp(self):
        """Runs before each test to create tables,
        sqlalchemy session and some sample data
        """
        fill_database(self)

    def tearDown(self):
        """Runs after each test to close the sqlalchemy session"""
        self.storage.close()

    def test_add_country(self):
        """Test adding a country to the database"""
        ken = Country(name='Kenya')

        self.assertNotIn(ken, self.storage.all())
        self.assertNotIn(ken, self.storage.all('Country'))

        self.storage.add(ken)
        self.storage.commit()

        self.assertIn(ken, self.storage.all())
        self.assertIn(ken, self.storage.all('Country'))

    def test_add_city(self):
        """Test adding a city to the database"""
        mek = City(name='Mekele', country_id=self.eth.id)

        self.assertNotIn(mek, self.storage.all())
        self.assertNotIn(mek, self.storage.all('City'))

        self.storage.add(mek)
        self.storage.commit()

        self.assertIn(mek, self.storage.all())
        self.assertIn(mek, self.storage.all('City'))

    def test_add_donor(self):
        """Test adding a donor to the database"""
        ken = Donor(username='KencKde',
                    email='ken@ex.com', password_hash='mjloghl',
                    phone_number='0987634599',
                    full_name='Ken', age=21,
                    gender='Male', blood_category='A+')

        self.assertNotIn(ken, self.storage.all())
        self.assertNotIn(ken, self.storage.all('Donor'))

        self.storage.add(ken)
        self.storage.commit()

        self.assertIn(ken, self.storage.all())
        self.assertIn(ken, self.storage.all('Donor'))

    def test_add_transfusion_center(self):
        """Test adding a transfusion_center to the database"""
        mol = TC(name='Moulay Ali Chrif',
                 email='mol@ex.com', password_hash='holatrop',
                 phone_number='0194129876', city_id=self.err.id)

        self.assertNotIn(mol, self.storage.all())
        self.assertNotIn(mol, self.storage.all('TransfusionCenter'))
        self.assertNotIn(mol, self.storage.all('TC'))

        self.storage.add(mol)
        self.storage.commit()

        self.assertIn(mol, self.storage.all())
        self.assertIn(mol, self.storage.all('TransfusionCenter'))
        self.assertIn(mol, self.storage.all('TC'))

    def test_add_blood_bag(self):
        """Test adding a blood_bag to the database"""
        bag = BloodBag(blood_category='AB-', quantity=20, situation='Stable',
                       center_id=self.sah.id)

        self.assertNotIn(bag, self.storage.all())
        self.assertNotIn(bag, self.storage.all('BloodBag'))

        self.storage.add(bag)
        self.storage.commit()

        self.assertIn(bag, self.storage.all())
        self.assertIn(bag, self.storage.all('BloodBag'))

    def test_add_all(self):
        """Test adding multiple entries at once with add_all()"""
        ken = Country(name='Kenya')
        mek = City(name='Mekele', country_id=self.eth.id)
        bln = Donor(username='blainoctocat',
                    email='bln@ex.com', password_hash='frtujh78',
                    phone_number='0812354760',
                    full_name='Blain', age=25,
                    gender='Male', blood_category='AB+')
        mol = TC(name='Moulay Ali Chrif',
                 email='mol@ex.com', password_hash='holatrop',
                 phone_number='0194129876', city_id=self.err.id)
        bag = BloodBag(blood_category='O-', quantity=6, situation='Critic',
                       center_id=self.sah.id)

        self.assertNotIn(ken, self.storage.all())
        self.assertNotIn(mek, self.storage.all())
        self.assertNotIn(bln, self.storage.all())
        self.assertNotIn(mol, self.storage.all())
        self.assertNotIn(bag, self.storage.all())

        self.storage.add_all([ken, mek, bln, mol, bag])
        self.storage.commit()

        self.assertIn(ken, self.storage.all())
        self.assertIn(mek, self.storage.all())
        self.assertIn(bln, self.storage.all())
        self.assertIn(mol, self.storage.all())
        self.assertIn(bag, self.storage.all())


class TestStorageDelete(unittest.TestCase):
    """Test Storage delete() and delete_all() methods"""

    def setUp(self):
        """Runs before each test to create tables,
        sqlalchemy session and some sample data
        """
        fill_database(self)

    def tearDown(self):
        """Runs after each test to close the sqlalchemy session"""
        self.storage.close()

    def test_delete_blood_bag(self):
        """Test deleting a BloodBag instance"""
        self.assertIn(self.bag, self.storage.all())

        self.storage.delete(self.bag)
        self.storage.commit()

        self.assertNotIn(self.bag, self.storage.all())

    def test_delete_donor(self):
        """Test deleting a Donor instance"""
        self.assertIn(self.ych, self.storage.all())

        self.storage.delete(self.ych)
        self.storage.commit()

        self.assertNotIn(self.ych, self.storage.all())

    def test_delete_transfusion_center(self):
        """Test deleting a TransfusionCenter instance and verify cascade"""
        self.assertIn(self.sah, self.storage.all())
        self.assertIn(self.bag, self.storage.all())

        self.storage.delete(self.sah)
        self.storage.commit()

        self.assertNotIn(self.sah, self.storage.all())
        self.assertNotIn(self.bag, self.storage.all())

    def test_delete_city(self):
        """Test deleting a City instance and verify cascade"""
        self.assertIn(self.err, self.storage.all())
        self.assertIn(self.sah, self.storage.all())
        self.assertIn(self.bag, self.storage.all())

        self.storage.delete(self.err)
        self.storage.commit()

        self.assertNotIn(self.err, self.storage.all())
        self.assertNotIn(self.sah, self.storage.all())
        self.assertNotIn(self.bag, self.storage.all())

    def test_delete_country(self):
        """Test deleting a Country instance and verify cascade"""
        self.assertIn(self.mor, self.storage.all())
        self.assertIn(self.err, self.storage.all())
        self.assertIn(self.sah, self.storage.all())
        self.assertIn(self.bag, self.storage.all())

        self.storage.delete(self.mor)
        self.storage.commit()

        self.assertNotIn(self.mor, self.storage.all())
        self.assertNotIn(self.err, self.storage.all())
        self.assertNotIn(self.sah, self.storage.all())
        self.assertNotIn(self.bag, self.storage.all())

    def test_delete_all(self):
        """Test delete_all() method"""
        country_1 = Country(name='Ordinn')
        country_2 = Country(name='Firone')
        donor_1 = Donor(username='don_1',
                       email='d1@ex.com', password_hash='oojho87',
                       phone_number='0605439008',
                       full_name='Donor 1', age=28,
                       gender='Female', blood_category='B-')
        donor_2 = Donor(username='don_2',
                       email='d2@ex.com', password_hash='iuyhg60',
                       phone_number='0406589808',
                       full_name='Donor 2', age=18,
                       gender='Male', blood_category='O-')

        self.storage.add_all([country_1, country_2, donor_1, donor_2])
        self.storage.commit()

        self.assertIn(country_1, self.storage.all())
        self.assertIn(country_2, self.storage.all())
        self.assertIn(donor_1, self.storage.all())
        self.assertIn(donor_2, self.storage.all())

        self.storage.delete_all([country_1, country_2, donor_1, donor_2])
        self.storage.commit()

        self.assertNotIn(country_1, self.storage.all())
        self.assertNotIn(country_2, self.storage.all())
        self.assertNotIn(donor_1, self.storage.all())
        self.assertNotIn(donor_2, self.storage.all())


class TestStorageGet(unittest.TestCase):
    """Test Storage get() method"""

    @classmethod
    def setUpClass(cls):
        """Runs at class beginning to create tables,
        sqlalchemy session and some sample data
        """
        fill_database(cls)

    @classmethod
    def tearDownClass(cls):
        """Runs at class ending to close the sqlalchemy session"""
        cls.storage.close()

    def test_get_with_country(self):
        """Test get() method with 'Country'"""
        morocco = self.storage.get('Country', 1)
        ethiopia = self.storage.get('Country', 2)

        self.assertEqual(morocco, self.mor)
        self.assertEqual(ethiopia, self.eth)

    def test_get_with_city(self):
        """Test get() method with 'City'"""
        errachidia = self.storage.get('City', 1)

        self.assertEqual(errachidia, self.err)

    def test_get_with_donor(self):
        """Test get() method with 'Donor'"""
        donor = self.storage.get('Donor', 1)

        self.assertEqual(donor, self.ych)

    def test_get_with_transfusion_center(self):
        """Test get() method with 'TransfusionCenter'"""
        sahraoui = self.storage.get('TransfusionCenter', 1)
        sahraoui_tc = self.storage.get('TC', 1)

        self.assertEqual(sahraoui, self.sah)
        self.assertEqual(sahraoui_tc, self.sah)

    def test_get_with_blood_bag(self):
        """Test get() method with 'BloodBag'"""
        blood_bag = self.storage.get('BloodBag', 1)

        self.assertEqual(blood_bag, self.bag)
