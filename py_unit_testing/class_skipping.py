"""Module for class skipping unit test """

import unittest

@unittest.skip('Skipping class')
class SkippedTestClass(unittest.TestCase):
    """Skipping test class """

    def test_not_run(self) -> None:
        """test not run method """

if __name__ == '__main__':
    unittest.main()


# Command line execution, use following
# python -m unittest ClassSkipping -v
