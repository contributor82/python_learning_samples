"""Module for expected failure test case"""

import unittest

class ExpectedFailureClass(unittest.TestCase):
    """Expected failure class """

    @unittest.expectedFailure
    def test_fail(self) -> None:
        """test fail method """
        self.assertEqual(1,0, 'Broken')

    @unittest.skip('object does not have attribute')
    def skip_unless_has_attr(self, obj: object, attr: str) -> (object):
        """Skip unless has attribute method """
        test_result : AttributeError
        reason: str = ''
        try:
            if hasattr(obj, attr):
                return 'Hello World!'
            reason = f'{obj!r} does not have {attr!r}'
        except AttributeError as attr_error:
            test_result = attr_error
            self.assertEqual(test_result.args[0], '')
        return unittest.skip(reason)


if __name__ == '__main__':
    unittest.main()

# Command line execution
# python -m unittest expected_failure_test -v
