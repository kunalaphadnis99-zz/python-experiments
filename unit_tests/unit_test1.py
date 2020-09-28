import unittest

from unit_tests import testing_functions


class Tests(unittest.TestCase):
    def test_add_numbers(self):
        num1, num2 = 10, 10
        result = testing_functions.add_numbers(num1, num2)
        self.assertEqual(20, result)

    def test_divide_numbers_succeeds(self):
        num1, num2 = 10, 10
        result = testing_functions.divide_numbers(num1, num2)
        self.assertEqual(1, result)

    def test_divide_numbers_fails(self):
        num1, num2 = 10, 0
        result = testing_functions.divide_numbers(num1, num2)
        # self.assertEqual(ZeroDivisionError, type(result))
        self.assertTrue(isinstance(result, ZeroDivisionError))


unittest.main()
