#!/usr/bin/python3
"""Test script
Run with: python3 -m tests.test
"""
from db import storage
from db.models.country import Country
from db.models.city import City
from db.models.transfusion_center import TransfusionCenter as TC
from db.models.donor import Donor
from db.models.blood_bag import BloodBag


mor = Country(name='Morrocco')
chili = Country(name='Chili')
storage.add_all([mor, chili])
storage.commit()

err = City(name='Errachidia', country_id=mor.id)
storage.add(err)
storage.commit()

sah = TC(name='Sahraoui', email='sah@ex.com', password_hash='nkmjuh',
         city_id=err.id)
storage.add(sah)
storage.commit()

ych = Donor(username='youcha', email='ych@ex.com', password_hash='poulkll',
            full_name='Youssef Charif', age=21,
            gender='Male', blood_category='O-')
storage.add(ych)
storage.commit()

bag = BloodBag(blood_category='O-', quantity=6, situation='Critic',
               center_id=sah.id)
storage.add(bag)
storage.commit()

ych.followed_centers.append(sah)

storage.commit()
# storage.show()
