"""Module for test iteration using subtest"""
import unittest
# Distinguishing test iteration using subtests
class Numbertests(unittest.TestCase):
    """Number tests class"""

    def test_even(self) -> None:
        """test even number method"""
        # Without using subtest, the failure would stop after
        # first execution and gives less details to diagnose the failure.
        test_result: AssertionError
        try:
            for i in range(0,6):
                self.assertEqual(i % 2,0)
                # with self.assertRaises(AssertionError) as assertion_error:
                #      test_result = assertion_error
        except AssertionError as test_even_assertion_error:
            test_result = test_even_assertion_error
            self.assertEqual(str(test_result.args[0]), '1 != 0')


    def test_even_subtest(self) -> None:
        """Test even subtest method """
        # Using subtest, the failure would display till the end
        # with more detail information to diagnose the failure.
        test_result: AssertionError
        try:
            for i in range(0,6):
                print('i = ', i, ' i % 2 = ', (i %2))
                with self.subTest(i=i):
                    self.assertEqual(i % 2, 0)
        except AssertionError as test_even_subtest_assertion_err:
            test_result = test_even_subtest_assertion_err
            self.assertEqual(str(test_result.args[0]), '1 != 0')


if __name__ == '__main__':
    unittest.main()
