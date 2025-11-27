import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    
    def test_addition(self):
        """Test normal addition cases."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_with_large_numbers(self):
        """Test addition with large numbers."""
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    
    def test_subtraction(self):
        """Test normal subtraction cases."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(0, 10), -10)

    
    def test_multiplication(self):
        """Test normal multiplication cases."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiplication_with_large_numbers(self):
        """Test multiplication using large values."""
        self.assertEqual(self.calc.multiply(10000, 10000), 100000000)

    
    def test_division(self):
        """Test normal division."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7/3)

    def test_division_by_zero(self):
        """Ensure dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_with_negative_numbers(self):
        """Test division with negative values."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)


if __name__ == "__main__":
    unittest.main()
