#!/usr/bin/python3
import unittest
from add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_with_valid_ints(self):
        self.assertEqual(add_numbers(2, 5), 7)

    def test_with_valid_floats(self):
        self.assertEqual(add_numbers(2.3, 4.5), 6.8)

    def test_with_invalid_data(self):
        self.assertRaises(TypeError, add_numbers, "two", 5)

    def test_with_none_input(self):
        with self.assertRaises(TypeError):
            add_numbers(10, None)

    def test_with_one_arg_missing(self):
        with self.assertRaises(TypeError):
            add_numbers(2)
