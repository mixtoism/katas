import unittest
from chain_adding.chain_adder import adder


class ChainAdded(unittest.TestCase):
    def test_single_parameter_returns_received_number(self):
        self.assertEqual(adder(1), 1)
        self.assertEqual(adder(2), 2)

    def test_multiple_parameter_should_return_sum(self):
        self.assertEqual(adder(1)(2), 3)
        self.assertEqual(adder(1)(2)(3), 6)

    def test_adder_should_be_able_to_add(self):
        self.assertEqual(adder(1) + 1, 2)

    def test_adder_should_be_able_to_add_other_adders(self):
        self.assertEqual(adder(1)(2) + adder(3)(4), 10)
