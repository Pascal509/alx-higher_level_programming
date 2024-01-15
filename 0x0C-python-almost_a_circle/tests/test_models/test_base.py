#!/usr/bin/python3
"""Modules for base unit testing"""
import unittest
from models.base import Base

class Testbase(unittest.TestCase):
    """Test Base class"""
    def  setUp(self):
        """imports module and instantiates class"""
        self.a = Base()
        self.b = Base(24)

    def test_isEquals(self):
        """Test is case equals to output"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 24)

    def test_isinstance(self):
        """Checks for datatypes"""
        a = Base()
        b = Base()
        self.assertNotisinstance(a, int)


if __name__ == '__main__':
    unittest.main()
