#!/usr/bin/python3
"""Initialize tests for database"""
from db.engine.storage import Storage
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter as TC
from db.models.donor import Donor
from db.models.blood_bag import BloodBag


def fill_database(self, storage=None):
    """Return a ready test storage"""
    if not storage:
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
