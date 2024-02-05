#!/usr/bin/python3
"""Unittest module to ensure proper working of BaseModel class"""
from datetime import datetime
from db.models.base import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Test features of BaseModel class"""

    def setUp(self):
        """Run before each test function"""
        self.basic = BaseModel()
        self.with_name = BaseModel(name='I am Root')
        self.multi = BaseModel(one=1, two='two', three_point_five=3.5)

    def tearDown(self):
        """Run after each test function"""
        BaseModel._BaseModel__counter = 1

    def test_id(self):
        """Test id attribute"""
        self.assertEqual(self.basic.id, 1)
        self.assertEqual(self.with_name.id, 2)
        self.assertEqual(self.multi.id, 3)

    @staticmethod
    def ftime(time):
        """Return a string representation of datetime object"""
        return time.strftime('%Y/%m/%d %H:%M:%S')

    def test_times(self):
        """Test created_at and updated_at attributes"""
        self.assertIs(type(self.basic.created_at), datetime)
        self.assertIs(type(self.basic.updated_at), datetime)

        self.assertEqual(self.ftime(self.basic.created_at),
                         self.ftime(self.basic.updated_at))

        late = BaseModel()
        self.assertNotEqual(self.basic.created_at, late.created_at)
        self.assertNotEqual(self.basic.updated_at, late.updated_at)

    def test_to_dict(self):
        """Test to_dict() method"""
        basic_dict = {'id': 1,
                      'created_at': self.ftime(self.basic.created_at),
                      'updated_at': self.ftime(self.basic.updated_at)
                      }

        self.assertEqual(self.basic.to_dict(), basic_dict)

        with_name_dict = {'id': 2,
                          'name': 'I am Root',
                          'created_at': self.ftime(self.with_name.created_at),
                          'updated_at': self.ftime(self.with_name.updated_at)
                          }

        self.assertEqual(self.with_name.to_dict(), with_name_dict)

        multi_dict = {'id': 3,
                      'one': 1,
                      'two': 'two',
                      'three_point_five': 3.5,
                      'created_at': self.ftime(self.multi.created_at),
                      'updated_at': self.ftime(self.multi.updated_at)
                      }

        self.assertEqual(self.multi.to_dict(), multi_dict)

    def test_repr(self):
        """Test string representation of BaseModel instances"""
        string_basic = 'BaseModel :\n'
        string_basic += f'\tid = {self.basic.id} -> '
        created_at = self.ftime(self.basic.created_at)
        string_basic += f'created_at: {created_at} / '
        updated_at = self.ftime(self.basic.updated_at)
        string_basic += f'updated_at: {updated_at}'

        self.assertEqual(string_basic, repr(self.basic))
        self.assertEqual(string_basic, str(self.basic))

        string_with_name = 'BaseModel :\n'
        string_with_name += f'\tid = {self.with_name.id} -> '
        string_with_name += f'name: I am Root / '
        created_at = self.ftime(self.with_name.created_at)
        string_with_name += f'created_at: {created_at} / '
        updated_at = self.ftime(self.with_name.updated_at)
        string_with_name += f'updated_at: {updated_at}'

        self.assertEqual(string_with_name, repr(self.with_name))
        self.assertEqual(string_with_name, str(self.with_name))

        string_multi = 'BaseModel :\n'
        string_multi += f'\tid = {self.multi.id} -> '
        created_at = self.ftime(self.multi.created_at)
        string_multi += f'created_at: {created_at} / '
        updated_at = self.ftime(self.multi.updated_at)
        string_multi += f'updated_at: {updated_at}'

        self.assertEqual(string_multi, repr(self.multi))
        self.assertEqual(string_multi, str(self.multi))
