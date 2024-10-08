# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated October 3, 2024

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: sm
"""

def classifyTriangle(a,b,c):
    if a is None or b is None or c is None:
        raise TypeError("Three inputs required")
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
    
    sides = [a,b,c]
    sides.sort()
    a = sides[0]
    b = sides[1]
    c = sides[2]

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if not(a + b > c and a + c > b and b + c > a):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'
