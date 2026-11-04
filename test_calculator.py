import unittest
from calculator import modulo, square


class TestCalculator(unittest.TestCase):

    def test_normal_modulo(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_exact_division(self):
        self.assertEqual(modulo(15, 5), 0)

    def test_negative_number(self):
        self.assertEqual(modulo(-10, 3), 2)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_square_positive(self):
        self.assertEqual(square(5), 25)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

    def test_square_fraction(self):
        self.assertEqual(square(2.5), 6.25)

if __name__ == "__main__":
    unittest.main()
