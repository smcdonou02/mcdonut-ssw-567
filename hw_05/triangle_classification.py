"""
SSW 567
Prof. Morgan
Homework 1: Triangle Classification
Author: Stephanie McDonough
09/23/2024
"""

import math

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its sides (a, b, c).
    Returns:
        - "Not valid side length" if any side length is invalid.
        - "Triangle is right triangle" if the triangle is a right triangle.
        - "Triangle is equilateral" if all sides are equal.
        - "Triangle is isosceles" if two sides are equal.
        - "Triangle is scalene" if all sides are different.
    """
    sides = [a, b, c]
    h = max(sides)
    sides.remove(h)
    if min(sides) <= 0:
        return "Not valid side length"
    if h == math.sqrt(sides[0]**2 + sides[1]**2):
        return "Triangle is right triangle"
    if a == b == c:
        return "Triangle is equilateral"
    if a == b or b == c or a == c:
        return "Triangle is isosceles"
    return "Triangle is scalene"
