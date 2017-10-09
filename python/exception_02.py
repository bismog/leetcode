#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest as ut
# import testtools as ut

# A simple function to illustrate
def parse_int(s):
    return int(s)

# class TestConversion(ut.TestCase):
#     def __init__(self):
#         super(TestConversion, self).__init__()
# 
#     #def test_bad_int(self):
#     def runTest(self):
#         self.assertRaises(ValueError, parse_int, 'N/A')

class TestConversion(ut.TestCase):
    def runTest(self):
        try:
            r = parse_int('N/A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

if __name__ == "__main__":
    ttt = TestConversion()
    # ttt.test_bad_int()
    ttt.runTest()

# import unittest
# 
# class Calculator:
# 
#     def mod(self, dividend, divisor):
#         remainder = dividend % divisor
#         quotient = (dividend - remainder) / divisor
#         return quotient, remainder
# 
# class CalculatorTest(unittest.TestCase):
# 
#     def test_mod_with_remainder(self):
#         cal = Calculator()
#         self.assertEqual(cal.mod(5, 3), (1, 2))
# 
#     def test_mod_without_remainder(self):
#         cal = Calculator()
#         self.assertEqual(cal.mod(8, 4), (1, 0))
# 
#     def test_mod_divide_by_zero(self):
#         cal = Calculator()
#         self.assertRaises(ZeroDivisionError, cal.mod, 7, 1)
# 
# if __name__ == '__main__':
#     unittest.main()  
