#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Defines unittest for max int"""

    def test_ordered_list(self):
        list_ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_ordered), 4)

    def test_unordered_list(self):
        list_unordered = [3, 4, 1, 2]
        self.assertEqual(max_integer(list_unordered), 4)

    def test_float_list(self):
        list_float = [3.7, 4.4, 1.2, 2.6]
        self.assertEqual(max_integer(list_float), 4.4)

    def test_int_float_list(self):
        list_int_float = [3, 4.4, 1, 2.6]
        self.assertEqual(max_integer(list_int_float), 4.4)

    def test_int_float_neg_list(self):
        list_int_float_neg = [-3, -4.4, 1, 2.6]
        self.assertEqual(max_integer(list_int_float_neg), 2.6)

    def test_unit_list(self):
        list_unit = [89]
        self.assertEqual(max_integer(list_unit), 89)

    def test_empty_list(self):
        list_empty = []
        self.assertEqual(max_integer(list_empty), None)

    def test_string(self):
        string = "sting"
        self.assertEqual(max_integer(string), 'r')

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
