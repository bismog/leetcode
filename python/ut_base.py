#!/usr/bin/env python
#encoding=utf-8

import unittest 

class RomanNumeralConverter(object): 
  """converter the Roman Number"""
  
  def __init__(self, roman_numeral): 
    """Constructor"""
    self.roman_numeral = roman_numeral 
    self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1} 

  def convert_to_decimal(self): 
    val = 0
    for char in self.roman_numeral: 
      val += self.digit_map[char] 
    return val 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
class RomanNumeralConverterTest(unittest.TestCase): 
  """test class"""
  def test_parsing_millenia(self): 
    value = RomanNumeralConverter("M") 
    self.assertEquals(1000, value.convert_to_decimal()) 

  def test_parsing_m_d(self): 
    value = RomanNumeralConverter(["M", 'D']) 
    self.assertEquals(1500, value.convert_to_decimal()) 

#  def test_parsing_m_d(self): 
#    value = RomanNumeralConverter(["M", 'd']) 
#    self.assertEquals(1500, value.convert_to_decimal()) 
    
if __name__ == "__main__": 
  unittest.main() 

