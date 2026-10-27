import unittest
from password_analyzer import analyze_password

class TestPasswordAnalyzer(unittest.TestCase):
    def test_weak_passwords(self):
        self.assertEqual(analyze_password("short"), "Weak")
        self.assertEqual(analyze_password("allletters"), "Weak")
        self.assertEqual(analyze_password("123456789"), "Weak")
        
    def test_medium_passwords(self):
        self.assertEqual(analyze_password("password123"), "Medium")
        self.assertEqual(analyze_password("12345678a"), "Medium")
        
    def test_strong_passwords(self):
        self.assertEqual(analyze_password("Strong!Pass1"), "Strong")
        self.assertEqual(analyze_password("h@cker99XYZ"), "Strong")
        
    def test_edge_cases(self):
        # Empty string should be handled gracefully
        self.assertEqual(analyze_password(""), "Weak")


if __name__ == '__main__':
    unittest.main()