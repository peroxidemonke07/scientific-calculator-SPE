import unittest
from unittest.mock import patch
from src.calculator import square_root, factorial, natural_logarithm, power

class TestCalculator(unittest.TestCase):

    @patch('builtins.input', return_value='4')
    def test_square_root_4(self, mock_input):
        result = square_root()
        self.assertEqual(result, 2.0)

# Test that a negative input to square_root raises a ValueError
    @patch('builtins.input', return_value='-5')
    def test_square_root_negative1(self, mock_input):
        with self.assertRaises(ValueError):
            square_root()

    @patch('builtins.input', return_value='5')
    def test_factorial_5(self, mock_input):
        result = factorial()
        self.assertEqual(result, 120)
    
    @patch('builtins.input', return_value='0')
    def test_factorial_0(self, mock_input):
        result = factorial()
        self.assertEqual(result, 1)
    
    @patch('builtins.input', return_value='1')
    def test_factorial_1(self, mock_input):
        result = factorial()
        self.assertEqual(result, 1)

# Test that a negative input to factorial raises a ValueError for factorial
    @patch('builtins.input', return_value='-1')
    def test_factorial_negative(self, mock_input):
        with self.assertRaises(ValueError):
            factorial()

# Test that a non-integer input to factorial raises a ValueError for factorial 
    @patch('builtins.input', return_value='3.5')
    def test_factorial_non_integer(self, mock_input):
        with self.assertRaises(ValueError):
            factorial()

    @patch('builtins.input', return_value='2')
    def test_natural_logarithm(self, mock_input):
        result = natural_logarithm()
        self.assertAlmostEqual(result, 0.6931, places=4)

# Test that a non-positive input raises a ValueError for natural_logarithm
    @patch('builtins.input', return_value='-2')
    def test_natural_logarithm_non_positive(self, mock_input):
        with self.assertRaises(ValueError):
            natural_logarithm()

    @patch('builtins.input', side_effect=['2', '3'])
    def test_power(self, mock_inputs):
        result = power()
        self.assertEqual(result, 8.0)

if __name__ == '__main__':
    unittest.main()
