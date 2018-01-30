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
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')
    
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 7), 'Isoceles', '5,5,7 is an Isoceles Triangle')
    
    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(5, 7, 5), 'Isoceles', '5,7,5 is an Isoceles Triangle')
    
    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(7, 5, 5), 'Isoceles', '7,7,5 is an Isoceles Triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 is a Scalene Triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(5, 4, 6), 'Scalene', '5,4,6 is a Scalene Triangle')

    def testStringInput(self):
        self.assertEqual(classifyTriangle('How', 'Are', 'You'), 'InvalidInput',
                          'Strings Input is Invalid')
    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','Cannot have negative side length')

    def testLargeInput(self):
        self.assertEqual(classifyTriangle(300,300,300),'InvalidInput','Defined as too big')
        
    def testDecimalInput(self):
        self.assertEqual(classifyTriangle(1.1, 1.1, 1.1), 'InvalidInput', 
                         'Triangle.py only accepts integers')

    def testNonZeroInvalidSides(self):
        self.assertEqual(classifyTriangle(1, 2, 7), 'NotATriangle', 
                         '1 + 2 !>= 7')

    def testZeroSides(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0 length side not possible')

    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

