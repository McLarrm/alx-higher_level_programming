#!/usr/bin/python3
""" Unit test for list of functions """


import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 8, 2]), 10)
        self.assertEqual(max_integer([100, 50, 25, 75]), 100)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -2]), -2)
        self.assertEqual(max_integer([-100, -50, -25, -75]), -25)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, 5, -8, 2]), 5)
        self.assertEqual(max_integer([100, -50, 25, -75]), 100)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-10, -10, -10, -10]), -10)

    def test_single_element(self):
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, max_integer, "12345")
        self.assertRaises(TypeError, max_integer, [1, 2, "3", 4])
        self.assertRaises(TypeError, max_integer, [1, 2, [3], 4])
        self.assertRaises(TypeError, max_integer, [1, 2, None, 4])

if __name__ == '__main__':
    unittest.main()
