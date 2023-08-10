"""Module for skipping tests and expected failure."""

from typing import NoReturn
import unittest
import sys

class SkipTestCase(unittest.TestCase):
    """Skip test case class """

    @unittest.skip("Demonstrating test case skipping")
    def test_nothing(self) -> NoReturn:
        """Test nothing method """
        self.fail("Test case fail shouldn't happen")

    # Giving a syntax error because mylib not present and there is no way to import it.
    # @unittest.skipIf(mylib.__version < (1,3), "Not supported in this library version")
    # def test_format(self):
    #     pass

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires windows")
    def test_windows_support(self) -> None:
        """Test windows support method """


    def external_resource_available(self) -> bool:
        """ External resource availability check method """
        return False

    def test_maybe_skipped(self) -> None:
        """ Test may be skipped method """
        if not self.external_resource_available():
            self.skipTest('External resource not available. ')


if __name__ == '__main__':
    unittest.main()


# For command line, use following
# python -m skipping_test_and_expected_failure -v
