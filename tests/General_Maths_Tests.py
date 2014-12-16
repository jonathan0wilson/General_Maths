import sys
import unittest

sys.path.insert(1, '.')
import General_Maths

class test_stuff(unittest.TestCase):

    def test_fibonacci_upto_ten(self):
        expected = [1, 1, 2, 3, 5, 8]
        actual = General_Maths.Fibonacci(10)
        self.assertEqual(expected, actual)

    def test_fibonacci_with_limit_less_than_one(self):
        self.assertRaises(General_Maths.OutOfRangeError,
                          General_Maths.Fibonacci, -1)

    def test_fibonacci_with_char(self):
        self.assertRaises(General_Maths.NotIntegerError,
                          General_Maths.Fibonacci, 'a')

    def test_fibonacci_with_non_int(self):
        self.assertRaises(General_Maths.NotIntegerError,
                          General_Maths.Fibonacci, 0.5)

    def test_reverse_number_with_123(self):
        self.assertEqual(General_Maths.Reverse_Int(123), 321)

    def test_reverse_number_with_non_integer(self):
        self.assertRaises(General_Maths.NotIntegerError,
                         General_Maths.Reverse_Int, 'a')

    def test_reverse_number_with_less_than_one(self):
        self.assertRaises(General_Maths.OutOfRangeError,
                          General_Maths.Reverse_Int, -1)

if __name__ == '__main__':
    unittest.main()
