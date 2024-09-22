'''
SSW 567
Prof. Morgan
Homework 1: Triangle Classification
Author: Stephanie McDonough
09/23/2024
'''
import math

def classify_triangle(a,b,c):
    sides = [a,b,c]
    h = max(sides)
    sides.remove(h)
    if min(sides) < 0:
        return "Not valid side length"
    if h == (math.sqrt(a**2 + b**2)):
        return "Triangle is right triangle"
    if a == b and b == c:
        return "Triangle is equilateral"
    elif a == b or b == c or a == c:
        return "Triangle is isosceles"
    elif a != b and b !=c and a != c:
        return "Triangle is scalene"
   

