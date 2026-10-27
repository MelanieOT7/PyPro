import unittest
from numerals import roman_to_int

class TestRomanConverter(unittest.TestCase):
    def test_single_numerals(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("M"), 1000)
        
    def test_addition_cases(self):
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("LVIII"), 58) # L = 50, V = 5, III = 3
        
    def test_subtraction_cases(self):
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994) # M=1000, CM=900, XC=90, IV=4



if __name__ == '__main__':
    unittest.main()