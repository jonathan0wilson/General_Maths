import sys
import unittest

sys.path.insert(1, '../')
import General_Maths

class test_stuff(unittest.TestCase):

    def test_fibonacci_upto_ten(self):
        expected = [1, 1, 2, 3, 5, 8]
        actual = General_Maths.Fibonacci(10)
        self.assertEqual(expected, actual)

    def test_fibonacci_with_limit_less_than_one(self):
        self.assertRaises(General_Maths.OutOfRangeError, General_Maths.Fibonacci, -1)


    def test_fibonacci_with_limitar(self):
        self.assertRaises(TypeError, General_Maths.Fibonacci, 'a')


if __name__ == '__main__':
    unittest.main()
