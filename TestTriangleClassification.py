import unittest
from TriangleClassification import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(1,2,3), "Triangle is scalene")
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(7,7,7), "Triangle is equilateral")
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(3,3,6), "Triangle is isosceles")
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3,4,5), "Triangle is right triangle")
    def test_negative_values(self):
        self.assertNotEqual(classify_triangle(-1,3,3), "Triangle is isosceles")

if __name__ == "__main__":
    unittest.main(verbosity=2)