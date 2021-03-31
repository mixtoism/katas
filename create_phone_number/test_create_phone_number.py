import unittest
import random
import re

from create_phone_number.create_phone_number import (
    create_phone_number,
    MUST_HAVE_LENGHT,
    MAX,
    MIN,
)


class TestCreatePhoneNumber(unittest.TestCase):
    def test_it_accepts_exactly_MUST_HAVE_LENGHT_integers(self):
        create_phone_number(random.choices(range(MIN, MAX + 1), k=MUST_HAVE_LENGHT))

    def test_if_less_than_MUST_HAVE_LENGHT_integers_raises_exception(self):
        with self.assertRaises(ValueError):
            create_phone_number(
                random.choices(range(MIN, MAX + 1), k=MUST_HAVE_LENGHT - 1)
            )

    def test_if_more_than_MUST_HAVE_LENGHT_integers_raises_exception(self):
        with self.assertRaises(ValueError):
            create_phone_number(
                random.choices(range(MIN, MAX + 1), k=MUST_HAVE_LENGHT + 1)
            )

    def test_not_accepts_numbers_more_than_max(self):
        with self.assertRaises(ValueError):
            create_phone_number(
                random.choices(range(MAX + 2, MAX + 3), k=MUST_HAVE_LENGHT)
            )

    def test_not_accepts_numbers_less_than_min(self):
        with self.assertRaises(ValueError):
            create_phone_number(
                random.choices(range(MIN - 3, MIN - 2), k=MUST_HAVE_LENGHT)
            )

    def test_it_follows_the_format(
        self,
    ):
        expression = re.compile("^\(\d\d\d\) \d\d\d-\d\d\d\d.*")
        numbers = random.choices(range(MIN, MAX + 1), k=MUST_HAVE_LENGHT)
        number = create_phone_number(numbers)
        print(number)
        self.assertTrue(expression.match(number))