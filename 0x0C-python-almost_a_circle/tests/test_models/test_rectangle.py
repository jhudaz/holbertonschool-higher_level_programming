#!/usr/bin/python3
"""
Unit test for the Rectangle class
"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
import json
import pep8


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class
    """

    def tearDown(self):
        """
        Reset the nb_objects
        """
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_documentation(self):
        """
        Test to see if documentation is correct and created
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "create"))
        self.assertTrue(Rectangle.create.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_json_string"))
        self.assertTrue(Rectangle.to_json_string.__doc__)
        self.assertTrue(hasattr(Rectangle, "from_json_string"))
        self.assertTrue(Rectangle.from_json_string.__doc__)
        self.assertTrue(hasattr(Rectangle, "save_to_file"))
        self.assertTrue(Rectangle.save_to_file.__doc__)
        self.assertTrue(hasattr(Rectangle, "load_from_file"))
        self.assertTrue(Rectangle.load_from_file.__doc__)

    def test_rectangle_id(self):
        """
        Testing the id of the new rectangle
        """
        Base._Base__nb_objects = 0
        r = Rectangle(5, 6)
        r1 = Rectangle(4, 3, 5)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(7, 8, 9, 10, 11)
        r5 = Rectangle(7, 8, 9, 10, -10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 3)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 11)
        self.assertEqual(r5.id, -10)

    def test_rectangle_arguments(self):
        """
        Testing the number of arguments send
        """
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(x=10, y=11)

    def test_rectangle_TypeError_width(self):
        """
        Testing the TypeError with the width arguments
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('Holberton', 2)
            Rectangle(True, 1)
            Rectangle([1, 2, 3], 2)
            Rectangle({"x": 1, "y": 3}, 2)
            Rectangle((4, 2), 2)
            Rectangle(None, 2)
            Rectangle(float('nan'), 2)
            Rectangle(float('inf'), 2)

    def test_rectangle_TypeError_height(self):
        """
        Testing the TypeError with the height argument
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 'Holberton')
            Rectangle(1, True)
            Rectangle(2, [1, 2, 3])
            Rectangle(2, {"x": 1, "y": 3})
            Rectangle(2, (4, 2))
            Rectangle(2, None)
            Rectangle(2, float('nan'))
            Rectangle(2, float('inf'))

    def test_rectangle_TypeError_x(self):
        """
        Testing the TypeError with the x argument
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, 'Holberton')
            Rectangle(1, 3, True)
            Rectangle(2, 3, [1, 2, 3])
            Rectangle(2, 3, {"x": 1, "y": 3})
            Rectangle(2, 3, (4, 2))
            Rectangle(2, 3, None)
            Rectangle(2, 3, float('nan'))
            Rectangle(2, 3, float('inf'))

    def test_rectangle_TypeError_y(self):
        """
        Testing the TypeError with the y argument
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, 'Holberton')
            Rectangle(1, 3, 4, True)
            Rectangle(2, 3, 4, [1, 2, 3])
            Rectangle(2, 3, 4, {"x": 1, "y": 3})
            Rectangle(2, 3, 4, (4, 2))
            Rectangle(2, 3, 4, None)
            Rectangle(2, 3, 4, float('nan'))
            Rectangle(2, 3, 4, float('inf'))

    def test_rectangle_ValueError_width(self):
        """
        Testing the ValueError with the width argument
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
            Rectangle(0, 2)
            Rectangle(height=2)

    def test_rectangle_ValueError_height(self):
        """
        Testing the ValueError with the height argument
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
            Rectangle(10, 0)
            Rectangle(width=2)

    def test_rectangle_ValueError_x(self):
        """
        Testing the ValueError with the x argument
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)
            Rectangle(10, 2, -100)
            Rectangle(10, 2, 0)

    def test_rectangle_ValueError_y(self):
        """
        Testing the ValueError with the y argument
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 1, -2)
            Rectangle(10, 2, 100, -200)
            Rectangle(10, 2, 1, 0)

    def test_rectangle_area(self):
        """
        Testing the area method
        """
        r = Rectangle(1, 2)
        r1 = Rectangle(3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9)
        r3 = Rectangle(10, 11, 12, 13, 14)
        r4 = Rectangle(9999999999999, 9999999999999)
        self.assertEqual(r.area(), 2)
        self.assertEqual(r1.area(), 3 * 4)
        self.assertEqual(r2.area(), 6 * 7)
        self.assertEqual(r3.area(), 10 * 11)
        self.assertEqual(r4.area(), 9999999999999 * 9999999999999)

    def test_rectangle_area_args(self):
        """
        Test the arguments with the method area
        """
        with self.assertRaises(TypeError):
            r = Rectangle()
            self.r.area(1)
