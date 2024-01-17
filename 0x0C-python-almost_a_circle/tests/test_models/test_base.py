#!/usr/bin/python3
"""Modules for base unit testing"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

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
        self.assertNotIsInstance(a, int)
        self.assertNotIsInstance(b, int)

    def tear_down(self):
        Base._Base__nb_objects = 0


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""
    def setUp(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.get_width(), 5)
        self.assertEqual(rectangle.get_height(), 10)
        self.assertEqual(rectangle.get_x(), 2)
        self.assertEqual(rectangle.get_y(), 3)
        self.assertEqual(rectangle.id, 1)

    def test_values(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.get_width(), 5)
        self.assertEqual(rectangle.get_height(), 10)
        self.assertEqual(rectangle.get_x(), 0)
        self.assertEqual(rectangle.get_y(), 0)
        self.assertIsNotNone(rectangle.id)

    def test_set(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)

        """ Test setting new values using setters"""
        rectangle.set_width(8)
        rectangle.set_height(12)
        rectangle.set_x(4)
        rectangle.set_y(6)

        self.assertEqual(rectangle.get_width(), 8)
        self.assertEqual(rectangle.get_height(), 12)
        self.assertEqual(rectangle.get_x(), 4)
        self.assertEqual(rectangle.get_y(), 6)

    def test_id_increment(self):
        rectangle1 = Rectangle(5, 10)
        rectangle2 = Rectangle(3, 6)

        self.assertNotEqual(rectangle1.id, rectangle2.id)

    def test_negative_values(self):
        """Test if negative values are allowed"""
        rectangle = Rectangle(-5, -10, -2, -3)

        self.assertEqual(rectangle.get_width(), -5)
        self.assertEqual(rectangle.get_height(), -10)
        self.assertEqual(rectangle.get_x(), -2)
        self.assertEqual(rectangle.get_y(), -3)

if __name__ == "__main__":
    unittest.main()
