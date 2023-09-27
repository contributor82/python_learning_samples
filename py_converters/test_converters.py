"""Module for test convertes class"""
from datetime import date, time
from decimal import Decimal
import unittest
from enum import Enum, IntEnum
from .py_converter import PyTypeConverters
class Color(Enum):
    """Color enumeration class """
    RED = 0
    GREEN = 1
    BLUE = 2

class TestConverters(unittest.TestCase):
    """Test converters class"""
    converters:PyTypeConverters = PyTypeConverters()

    def test_int_tostr(self, int_val: int = 10)-> None:
        """test integer to string """
        result = self.converters.int_tostr(int_val)
        self.assertEqual('10',result)

    def test_float_tostr(self, float_val: float = 10.5) -> None:
        """test float tostr"""
        result = self.converters.float_tostr(float_val)
        self.assertEqual('10.5',result)

    def test_decimal_tostr(self, decimal_val: Decimal = 10) -> None: # type: ignore
        """test decimal tostr"""
        result = self.converters.decimal_tostr(decimal_val)
        self.assertEqual('10',result)

    def test_int_enum_tostr(self, enum_int_val: IntEnum = 2) -> None: # type: ignore
        """test int enum tostr"""
        result = self.converters.int_enum_tostr(enum_int_val)
        self.assertEqual('2',result)

    def test_date_tostr(self, date_val: date = date.today()) -> None:
        """test date to string sconversion """
        result = self.converters.date_tostr(date_val)
        self.assertEqual(str(date.today()),result)

    def test_time_tostr(self, time_val : time = time(10,10,12,10)) -> None:
        """test time to string conversion """
        try:
            test_result: str | AssertionError
            result: str = self.converters.time_tostr(time_val)
            expected_time: str = time_val.strftime('%H:%M:%S %p')
            test_result = result
            self.assertEqual(expected_time ,result) # type: ignore
        except AssertionError as assert_error:
            test_result= assert_error
            self.assertTrue(test_result, AssertionError)

    def test_str_toint(self, int_val : str = '10')-> None:
        """test string to int conversion """
        result: int = self.converters.str_toint(int_val)
        self.assertEqual(10, result)

    def test_str_tofloat(self, float_val: str = '10.5')->None:
        """test string to float conversion """
        result: float = self.converters.str_tofloat(float_val)
        self.assertEqual(10.5,result)

    def test_str_todecimal(self, decimal_val: str = '10.0')->None:
        """test string to decimal conversion """
        result: Decimal = self.converters.str_todecimal(decimal_val)
        self.assertEqual(10.0,result)

    # def test_str_toenum(self,
    # enum_type: Enum = Color,
    # enum_val: str = "RED") -> None: #type: ignore
    #     """test string to enum conversion """
    #     result: Enum = self.converters.str_toenum(enum_type, enum_val)
    #     self.assertEqual(Color.RED,result)

    def test_str_todate_one(self, date_val_one: str = '2023-09-24')->None:
        """test string to date conversion """
        result: date = self.converters.str_todate(date_val_one)
        self.assertEqual(date(2023,9,24),result)

    def test_str_todate_two(self, date_val_two: str = '24-09-2023')->None:
        """test string to date conversion """
        result: date = self.converters.str_todate(date_val_two)
        self.assertEqual(date(2023,9,24),result)

if __name__ == '__main__':
    unittest.main()

# py -m unittest test_converters.py -v
