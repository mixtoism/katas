import unittest
from unittest.mock import Mock, MagicMock
from function_cache.function_cache import cache
from function_cache import function_cache


class TestFunctionCache(unittest.TestCase):
    def setUp(self) -> None:
        function_cache.__cache__ = {}
        return super().setUp()

    def test_single_parameter_first_call_calls_function(self):
        # GIVEN
        function = Mock()

        # WHEN
        cache(function, "EXAMPLE_PARAM")

        # ASSERT
        function.assert_called_once_with("EXAMPLE_PARAM")

    def test_single_parameter_first_call_calls_second_gets_from_cache(self):
        # GIVEN
        function = Mock()
        param = "EXAMPLE_PARAM"

        # WHEN
        cache(function, param)
        cache(function, param)

        # ASSERT
        self.assertEqual(function.call_count, 1)
        function.assert_called_once_with(param)

    def test_multiple_parameters_first_call_calls(self):
        function = Mock()
        params = (1, 2, 3)

        cache(function, *params)

        function.assert_called_once_with(*params)

    def test_multiple_parameters_first_call_calls_second_gets_from_cache(self):
        function = Mock()
        params = (1, 2, 3)

        cache(function, *params)
        cache(function, *params)

        self.assertEqual(function.call_count, 1)
        function.assert_called_once_with(*params)

    def test_kwargs_first_call_calls(self):
        function = Mock()
        params = {"par1": "a", "par2": "b"}

        cache(function, **params)
        function.assert_called_once_with(**params)

    def test_kwargs_first_call_calls_second_gets_from_cache(self):
        function = Mock()
        params = {"par1": "a", "par2": "b"}

        cache(function, **params)
        cache(function, **params)
        self.assertEqual(function.call_count, 1)
        function.assert_called_once_with(**params)

    def test_kwargs_order_is_not_important(self):
        function = Mock()
        params1 = {"par1": "a", "par2": "b"}
        params2 = {"par2": "b", "par1": "a"}

        cache(function, **params1)
        cache(function, **params2)
        self.assertEqual(function.call_count, 1)
        function.assert_called_once_with(**params1)

    def test_allow_parameters_with_different_types(self):
        function = Mock()
        params1 = {"par1": "1", "par2": "b"}
        params2 = {"par2": "b", "par1": 1}

        cache(function, **params1)
        cache(function, **params2)
        self.assertEqual(function.call_count, 2)

    def test_cache_is_faster(self):
        def fibonacci(x):
            if x == 1:
                return 1
            if x == 0:
                return 0
            return fibonacci(x - 1) + fibonacci(x - 2)

        def cache_fibonacci(x):
            if x == 1:
                return 1
            if x == 0:
                return 0
            return cache(cache_fibonacci, x - 1) + cache(cache_fibonacci, x - 2)

        from datetime import datetime
        import sys

        sys.setrecursionlimit(2147483647)
        init = datetime.now()
        fibonacci(100)
        end = datetime.now()
        no_cache_fibonacci_time = end - init

        init = datetime.now()
        cache_fibonacci(10000)
        end = datetime.now()
        cache_fibonacci_time = end - init
        print(no_cache_fibonacci_time)
        print(cache_fibonacci_time)
        self.assertLess(cache_fibonacci_time, no_cache_fibonacci_time)
