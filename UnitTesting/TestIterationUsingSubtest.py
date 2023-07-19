
# Distinguishing test iteration using subtests
import unittest

class Numbertests(unittest.TestCase): 

    # Without using subtest, the failure would stop after first execution and gives less details to diagnose the failure. 
    def test_even(self) -> None: 
        for i in range(0,6): 
            self.assertEqual(i % 2,0)

    # Using subtest, the failure would display till the end with more detail information to diagnose the failure. 
    def test_even_subtest(self) -> None: 
        for i in range(0,6):
            print("i = ", i, " i % 2 = ", (i %2))
            with self.subTest(i=i): 
                self.assertEqual(i % 2, 0)

if __name__ == '__main__': 
    unittest.main()