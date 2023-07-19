
import unittest

@unittest.skip("Skipping class")
class SkippedTestClass(unittest.TestCase): 
    def test_not_run(self) -> None: 
        pass


if __name__ == '__main__': 
    unittest.main()


# Command line execution, use following
# python -m unittest ClassSkipping -v