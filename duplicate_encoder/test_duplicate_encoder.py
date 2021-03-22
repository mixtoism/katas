import unittest
from unittest.mock import patch, Mock
from duplicate_encoder.duplicate_encoder import duplicate_encoder


class TestDuplicateEncoder(unittest.TestCase):
    def setUp(self):
        ...

    def test_single_char_should_return_open_parenthesis(self):
        self.assertEqual(duplicate_encoder("A"), "(")

    def test_if_chars_are_not_repeated_should_return_only_open_parenthesis(self):
        self.assertEqual(duplicate_encoder("AB"), "((")

    def test_if_chars_are_repeated_should_return_closed_parenthesis(self):
        self.assertEqual(duplicate_encoder("AA"), "))")

    def test_should_be_case_insensitive(self):
        self.assertEqual(duplicate_encoder("Aa"), "))")

    def test_empty_string_should_return_empty(self):
        self.assertEqual(duplicate_encoder(""), "")

