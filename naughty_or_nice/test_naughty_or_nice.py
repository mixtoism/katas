import unittest
from naughty_or_nice.main import naughty_or_nice, NAUGHTY, NICE, NEITHER


class TestNaughtyOrNice(unittest.TestCase):
    def setUp(self):
        ...

    def test_start_with_b_is_naughty(self):
        self.assertEqual(naughty_or_nice(["b"]), NAUGHTY)

    def test_start_with_f_is_naughty(self):
        self.assertEqual(naughty_or_nice(["f"]), NAUGHTY)

    def test_start_with_k_is_naughty(self):
        self.assertEqual(naughty_or_nice(["k"]), NAUGHTY)

    def test_start_with_g_is_nice(self):
        self.assertEqual(naughty_or_nice(["g"]), NICE)

    def test_start_with_s_is_nice(self):
        self.assertEqual(naughty_or_nice(["s"]), NICE)

    def test_start_with_n_is_nice(self):
        self.assertEqual(naughty_or_nice(["n"]), NICE)

    def test_start_with_other_letter_is_neither(self):
        self.assertEqual(naughty_or_nice(["a"]), NEITHER)

    def test_more_nice_than_naughty_actions_is_nice(self):
        self.assertEqual(naughty_or_nice(["b", "g", "s"]), NICE)
