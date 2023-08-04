# Skipping tests and expected failure. 
from typing import NoReturn
import unittest
import sys


class SkipTestCase(unittest.TestCase): 
    

    @unittest.skip("Demonstrating test case skipping")
    def test_nothing(self) -> NoReturn: 
        self.fail("Test case fail shouldn't happen")

    # Giving a syntax error because mylib not present and there is no way to import it. 
    # @unittest.skipIf(mylib.__version < (1,3), "Not supported in this library version")
    # def test_format(self): 
    #     pass

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires windows")
    def test_windows_support(self) -> None: 
        pass

    def external_resource_available(self) -> bool: 
        return False

    def test_maybe_skipped(self) -> None: 
        if not self.external_resource_available(): 
            self.skipTest('External resource not available. ')
        pass


if __name__ == '__main__': 
    unittest.main()


# For command line, use following
# python -m skipping_test_and_expected_failure -v  