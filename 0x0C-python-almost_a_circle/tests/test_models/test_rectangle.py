#!/usr/bin/python3
"""Modules for base unit testing"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""
    def setUp(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_values(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertIsNotNone(rectangle.id)

    def test_set(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)

        """ Test setting new values using setters"""
        rectangle.width = 8
        rectangle.height = 12
        rectangle.x = 4
        rectangle.y = 6

        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 6)

    def test_id_increment(self):
        rectangle1 = Rectangle(5, 10)
        rectangle2 = Rectangle(3, 6)

        self.assertNotEqual(rectangle1.id, rectangle2.id)

    def tearDown(self):
        Rectangle.__nb_objects = 0

class TestValidate(unittest.TestCase):
    """TestCase for Validation"""
    validate = Rectangle(5, 10)
    def test_validWidth(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)

    def test_validHeight(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5, 30)

    def test_valid_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "invalid", 30)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5, 30)

    def test_valid_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 30, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 30, -5)

class TestRectangleStr(unittest.TestCase):
    def test_str(self):
        string = Rectangle(width=5, height=3, x=2, y=1, id=1)
        expected_str = "[Rectangle] (1) 2/1 - 5/3"

        self.assertEqual(str(string), expected_str)


if __name__ == "__main__":
    unittest.main()
