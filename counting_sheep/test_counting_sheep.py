import unittest
from counting_sheep.count_sheep import count_sheep


class TestCountSheep(unittest.TestCase):
    def test_none_input(self):
        self.assertEqual(count_sheep(None), 0)

    def test_empty_list(self):
        self.assertEqual(count_sheep([]), 0)

    def test_correct_amount(self):
        self.assertEqual(count_sheep([True, False, None, True]), 2)