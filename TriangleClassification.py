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
    if h == (math.sqrt(a**2 + b**2)):
        print("Triangle is right triangle")
    if a == b and b == c:
        print("Triangle is equilateral")
    elif a == b or b == c or a == c:
        print("Triangle is isosceles")
    else:
        print("Triangle is scalene")
   




classify_triangle(3,4,5)

