import sys
import unittest

sys.path.insert(1, '.')
import General_Maths

class test_stuff(unittest.TestCase):

    def test_Sieve_upto_20(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        actual = General_Maths.Sieve_Of_Eratosthenes(20)
        self.assertEqual(expected, actual)

    def test_sieve_with_prime(self):
        expected = [2, 3, 5, 7, 11, 13, 17]
        actual = General_Maths.Sieve_Of_Eratosthenes(17)
        self.assertEqual(expected, actual)

    def test_sieve_with_non_int(self):
        self.assertRaises(General_Maths.NotIntegerError,
                          General_Maths.Sieve_Of_Eratosthenes, 'a')

    def test_sieve_with_limit_less_than_two(self):
        self.assertRaises(General_Maths.OutOfRangeError,
                          General_Maths.Sieve_Of_Eratosthenes, 1)

    def test_find_prime_factors_of_twenty(self):
        expected = { 2: 2, 5: 1}
        actual = General_Maths.find_prime_factors(20)
        self.assertEqual(expected, actual)

    def test_find_prime_factor_prime_returns_prime(self):
        expected = { 17: 1}
        actual = General_Maths.find_prime_factors(17)
        self.assertEqual(expected, actual)

    def test_find_prime_factors_with_char(self):
        self.assertRaises(General_Maths.NotIntegerError,
                          General_Maths.find_prime_factors, 'a')

    def test_find_prime_factors_with_less_than_two(self):
        self.assertRaises(General_Maths.OutOfRangeError,
                          General_Maths.find_prime_factors, -1)

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
