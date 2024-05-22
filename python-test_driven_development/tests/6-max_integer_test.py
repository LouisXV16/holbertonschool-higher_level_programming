#!/usr/bin/python3
"""unittest for the function max_integer"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test a list with all positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test a list with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 3, -2, 5, 0]), 5)

    def test_duplicates(self):
        """Test a list with duplicate numbers"""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_all_same(self):
        """Test a list with all same numbers"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.2]), 3.3)

    def test_including_zero(self):
        """Test a list that includes zero"""
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)

    def test_single_negative_number(self):
        """Test a list with a single negative number"""
        self.assertEqual(max_integer([-3]), -3)

    def test_none(self):
        """Test with None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_numbers(self):
        """Test a list with non-number elements"""
        with self.assertRaises(TypeError):
            max_integer(['a', 1, 'b', 2])

if __name__ == '__main__':
    unittest.main()

