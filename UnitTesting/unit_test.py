"""Module for unit testing """
import sys

sys.path.append('../StringOperations')
from string_methods import StringMethods
import unittest


# To have python detect written test cases,
# the method name should start with 'test' as prefix
class TestStringMethods(unittest.TestCase):
    """Test string methods class """
    def test_string_method_instance(self) -> None:
        """Test string method class instance method """
        smInstance = StringMethods()
        self.assertIsInstance(smInstance, StringMethods)


    def test_upper(self) -> None:
        """Test string upper method """
        # Using AssertEqual
        self.assertEqual('String'.upper(), "STRING")


    def test_isupper(self) -> None:
        """testing is string upper method """
        # Using AssertTrue
        self.assertTrue('STRING'.isupper())
        self.assertFalse('String'.isupper())

    def test_split(self) -> None:
        """ Testing string split method """
        # Using Assert raise for exception case
        input_str: str = 'Hello World!'
        self.assertEqual(input_str.split(), ['Hello', 'World'])

        with self.assertRaises(TypeError):
            input_str.split(2)

if __name__ == '__main__':
    unittest.main()

# Command line option to run test as
# Change directory first and then try following commands
# python -m unittest unit_test.py
# Enables higher level of verbosity when adding -v
# python -m unittest unit_test.py -v

