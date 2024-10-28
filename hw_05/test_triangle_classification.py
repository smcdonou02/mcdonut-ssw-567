"""
SSW 567
Prof. Morgan
Homework 1: Triangle Classification
Author: Stephanie McDonough
09/23/2024

Unit tests for the classify_triangle function in the triangle_classification module.
"""

import unittest
from triangle_classification import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    """Test cases for the classify_triangle function."""

    def test_scalene_triangle(self):
        """Test for scalene triangle (all sides are different)."""
        self.assertEqual(classify_triangle(1, 2, 3), "Triangle is scalene")

    def test_equilateral_triangle(self):
        """Test for equilateral triangle (all sides are equal)."""
        self.assertEqual(classify_triangle(7, 7, 7), "Triangle is equilateral")

    def test_isosceles_triangle(self):
        """Test for isosceles triangle (two sides are equal)."""
        self.assertEqual(classify_triangle(3, 3, 6), "Triangle is isosceles")

    def test_right_triangle(self):
        """Test for right triangle (satisfies the Pythagorean theorem)."""
        self.assertEqual(classify_triangle(3, 4, 5), "Triangle is right triangle")

    def test_negative_values(self):
        """Test for invalid triangle with negative side length."""
        self.assertNotEqual(classify_triangle(-1, 3, 3), "Triangle is isosceles")

if __name__ == "__main__":
    unittest.main(verbosity=2)
