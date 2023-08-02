import unittest

# To have python detect written test cases, the method name should start with 'test' as prefix

import sys
sys.path.append(r"\StringOperations")
from string_methods import StringMethods


class TestStringMethods(unittest.TestCase): 

    def test_string_method_instance(self) -> None: 
        smInstance = StringMethods()
        self.assertIsInstance(smInstance, StringMethods)

    # Using AssertEqual
    def test_upper(self) -> None: 
        self.assertEqual('String'.upper(), "STRING")

    # Using AssertTrue
    def test_isupper(self) -> None: 
        self.assertTrue('STRING'.isupper())
        self.assertFalse('String'.isupper())
    
    # Using Assert raise for exception case
    def test_split(self) -> None: 
        str = 'Hello World'
        self.assertEqual(str.split(), ['Hello', 'World'])
    
        with self.assertRaises(TypeError): 
            str.split(2)
    
if __name__ == '__main__':
    unittest.main()

# Command line option to run test as 
# Change directory first and then try following commands 
# python -m unittest UnitTest.py
# Enables higher level of verbosity when adding -v
# python -m unittest UnitTest.py -v  

    
