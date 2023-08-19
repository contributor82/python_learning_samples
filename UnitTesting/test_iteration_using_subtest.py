"""Module for test iteration using subtest"""
# Distinguishing test iteration using subtests
import unittest

class Numbertests(unittest.TestCase):
    """Number tests class"""

    def test_even(self) -> None:
        """test even number method"""
        # Without using subtest, the failure would stop after
        # first execution and gives less details to diagnose the failure.
        for i in range(0,6):
            self.assertEqual(i % 2,0)


    def test_even_subtest(self) -> None:
        """Test even subtest method """
        # Using subtest, the failure would display till the end
        # with more detail information to diagnose the failure.
        for i in range(0,6):
            print('i = ', i, ' i % 2 = ', (i %2))
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

if __name__ == '__main__':
    unittest.main()
