"""Module for expected failure test case"""

import unittest

class ExpectedFailureClass(unittest.TestCase):
    """Expected failure class """

    @unittest.expectedFailure
    def test_fail(self) -> None:
        """test fail method """
        self.assertEqual(1,0, 'Broken')

    def skip_unless_has_attr(self, obj: object, attr: str) -> (object):
        """Skip unless has attribute method """
        if hasattr(obj, attr):
            return lambda func: func
        reason: str = '{obj!r} does not have {attr!r}'
        return unittest.skip(reason)


if __name__ == '__main__':
    unittest.main()

# Command line execution
# python -m unittest expected_failure_test -v
