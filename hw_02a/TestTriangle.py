# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    #define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5,7,9),'Scalene', "5,7,9 should be scalene")

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(5,5,10), 'Isoceles', '5,5,10 should be isoceles')

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(201,4,5),'InvalidInput','Side A should not be greater than 200')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(3,201,5),'InvalidInput','Side B should not be greater than 200')
    
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(3,4,201),'InvalidInput','Side C should not be greater than 200')
    
    def testInvalidInputNegativeA(self): 
        self.assertEqual(classifyTriangle(-3,4,5),'InvalidInput','Side A should not be negative value')

    def testInvalidInputNegativeB(self): 
        self.assertEqual(classifyTriangle(3,-4,5),'InvalidInput','Side B should not be negative value')
    
    def testInvalidInputNegativeC(self): 
        self.assertEqual(classifyTriangle(3,4,-5),'InvalidInput','Side C should not be negative value')

    def testInvalidInputNotIntA(self): 
        self.assertEqual(classifyTriangle("3",4,5),'InvalidInput','Side A should be an integer')

    def testInvalidInputNotIntB(self): 
        self.assertEqual(classifyTriangle(3,"4",5),'InvalidInput','Side B should be an integer')

    def testInvalidInputNotIntC(self): 
        self.assertEqual(classifyTriangle(3,4,"5"),'InvalidInput','Side C should be an integer')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

