# Expected failure test case
import unittest

class ExpectedFailureClass(unittest.TestCase): 

    @unittest.expectedFailure
    def test_fail(self) -> None: 
        self.assertEqual(1,0, "Broken")

    def SkipUnlessHasattr(obj, attr): 
        if hasattr(obj, attr): 
            return lambda func: func 
        return unittest.skip("{!r} doesn't have {!r} ".format(obj,attr))


if __name__ == '__main__': 
    unittest.main()


# Command line execution 
# python -m unittest ExpectedFailureTest -v