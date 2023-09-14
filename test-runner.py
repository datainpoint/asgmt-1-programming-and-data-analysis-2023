import unittest
import importlib

class TestAssignmentOne(unittest.TestCase):
    def test_01_use_abs_function(self):
        self.assertEqual(asgmt.use_abs_function(-2), 2)
        self.assertEqual(asgmt.use_abs_function(-3), 3)
        self.assertEqual(asgmt.use_abs_function(0), 0)
        self.assertEqual(asgmt.use_abs_function(2), 2)
        self.assertEqual(asgmt.use_abs_function(3), 3)
    def test_02_use_pow_function(self):
        self.assertEqual(asgmt.use_pow_function(-2, 3), -8)
        self.assertEqual(asgmt.use_pow_function(-3, 2), 9)
        self.assertEqual(asgmt.use_pow_function(0, 2), 0)
        self.assertEqual(asgmt.use_pow_function(2, 3), 8)
        self.assertEqual(asgmt.use_pow_function(3, 2), 9)
    def test_03_use_round_function(self):
        self.assertEqual(asgmt.use_round_function(2.71828, 3), 2.718)
        self.assertEqual(asgmt.use_round_function(2.71828, 4), 2.7183)
        self.assertEqual(asgmt.use_round_function(3.141592, 2), 3.14)
        self.assertEqual(asgmt.use_round_function(3.141592, 5), 3.14159)
    def test_04_use_bin_function(self):
        self.assertEqual(asgmt.use_bin_function(0), '0b0')
        self.assertEqual(asgmt.use_bin_function(1), '0b1')
        self.assertEqual(asgmt.use_bin_function(2), '0b10')
        self.assertEqual(asgmt.use_bin_function(3), '0b11')
        self.assertEqual(asgmt.use_bin_function(4), '0b100')
        self.assertEqual(asgmt.use_bin_function(5), '0b101')
    def test_05_use_bool_function(self):
        self.assertFalse(asgmt.use_bool_function(0))
        self.assertTrue(asgmt.use_bool_function(1))
        self.assertTrue(asgmt.use_bool_function(2))
        self.assertTrue(asgmt.use_bool_function(3))
        self.assertTrue(asgmt.use_bool_function(4))
    def test_06_calculate_bmi(self):
        self.assertGreaterEqual(asgmt.calculate_bmi(216, 147), 31)
        self.assertGreaterEqual(asgmt.calculate_bmi(206, 113), 26)
        self.assertGreaterEqual(asgmt.calculate_bmi(211, 110), 24)
    def test_07_format_integer_with_dollar_sign_and_commas(self):
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000), "$1,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000), "$1,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000000), "$1,000,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(10000), "$10,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(100000), "$100,000")
    def test_08_is_positive(self):
        self.assertFalse(asgmt.is_positive(-2))
        self.assertFalse(asgmt.is_positive(-1))
        self.assertFalse(asgmt.is_positive(0))
        self.assertTrue(asgmt.is_positive(1))
        self.assertTrue(asgmt.is_positive(2))
    def test_09_is_even(self):
        self.assertFalse(asgmt.is_even(1))
        self.assertFalse(asgmt.is_even(3))
        self.assertFalse(asgmt.is_even(5))
        self.assertTrue(asgmt.is_even(0))
        self.assertTrue(asgmt.is_even(2))
    def test_10_are_vowels_contained(self):
        self.assertFalse(asgmt.are_vowels_contained('pythn'))
        self.assertFalse(asgmt.are_vowels_contained('ncnd'))
        self.assertFalse(asgmt.are_vowels_contained('rtclt'))
        self.assertTrue(asgmt.are_vowels_contained('anaconda'))
        self.assertTrue(asgmt.are_vowels_contained('reticulate'))

asgmt = importlib.import_module("asgmt-one")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentOne)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))