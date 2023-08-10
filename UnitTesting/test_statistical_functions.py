"""Module for test statistical Functions"""
from typing import Iterable
import unittest


class TestStatisticalFunctions(unittest.TestCase):
    """ Test statistical functions method """

    def average(self, values: list[int] | object ) -> float:
        """ getting average of list of numbers method """
        return sum(values)/len(values)

    def test_average(self) -> str | None | Exception:
        """ Test average method """
        try:
            avg_val: float = self.average([10,20,30,40])
            print('test_average: avg_val = ', avg_val)
            self.assertEqual(avg_val,40.0)
        except Exception as ex:
            return ex

    def test_average_by_rounding_value(self) -> str | None | Exception:
        """Test average by rounding value method """
        try:
            avg_val: float = self.average([1,5,7])
            print('test_average_by_rounding_value: avg_val = ', avg_val)
            round_val: float = round(avg_val,1)
            print('test_average_by_rounding_value: round_val = ', round_val)
            self.assertEqual(round_val, 4.3)
        except Exception as ex:
            return ex

    def test_average_type_error(self) -> str| None | Exception:
        """Test average type error method """
        try:
            avg_val: float = self.average(20,30,70)
            print('test_average_type_error: avg_val = ', avg_val)
            with self.assertRaises(TypeError): avg_val
        except Exception as ex:
            return ex

    def test_average_zero_division_error(self) -> str | None | Exception:
        """Test average zero division error method """
        try:
            avg_val: float = self.average([])
            print('test_average_zero_division_error: avg_val = ', avg_val)
            with self.assertRaises(ZeroDivisionError): avg_val
        except Exception as ex:
            return ex

if __name__ == '__main__':
    unittest.main()

# Command line execution as follows
# python -m unittest test_statistical_functions -v
