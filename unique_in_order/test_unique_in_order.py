import unittest
from unittest.case import skip
from unique_in_order.unique_in_order import unique_in_order


class TestUniqueInOrder(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_if_not_repeated_returns_same_string_as_list(self):
        self.assertEquals(unique_in_order("ABC"), ["A", "B", "C"])

    def test_if_not_repeated_returns_same_list(self):
        self.assertEquals(unique_in_order([1, 2, 3]), [1, 2, 3])

    def test_if_inmediately_repeated_omit(self):
        self.assertEquals(unique_in_order([1, 2, 2]), [1, 2])

    def test_if_empty_input_return_empty(self):
        self.assertEquals(unique_in_order([]), [])

    def test_if_empty_string_return_empy(self):
        self.assertEquals(unique_in_order(""), [])
