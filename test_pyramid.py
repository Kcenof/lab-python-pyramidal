import unittest
from app import calculate_pyramidal_number

class TestPyramidalCalculation(unittest.TestCase):

    def test_standard_cases(self):
        self.assertEqual(calculate_pyramidal_number(1), 1)
        self.assertEqual(calculate_pyramidal_number(2), 4)
        self.assertEqual(calculate_pyramidal_number(3), 10)
        self.assertEqual(calculate_pyramidal_number(4), 20)

    def test_zero_case(self):
        self.assertEqual(calculate_pyramidal_number(0), 0)

    def test_negative_exception(self):
        with self.assertRaises(ValueError):
            calculate_pyramidal_number(-1)
        
        with self.assertRaises(ValueError):
            calculate_pyramidal_number(-50)

if __name__ == '__main__':
    unittest.main()