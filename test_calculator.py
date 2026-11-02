import unittest
from calculator import modulo


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


if __name__ == "__main__":
    unittest.main()
