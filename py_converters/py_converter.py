"""Module for python type converters"""

from datetime import date, time
from decimal import Decimal
from enum import Enum, IntEnum
import re as regExp

# YET TO BE VERIFIED.
class Color(Enum):
    """Color enumeration class """
    RED = 0
    GREEN = 1
    BLUE = 2


class PyTypeConverters:
    """Py Type Converters"""

    def int_tostr(self, int_val:int)-> str:
        """Int to string conversion """
        return  str(int_val)

    def float_tostr(self, float_val:float)-> str:
        """Float to string conversion """
        return  str(float_val)

    def decimal_tostr(self, decimal_val:Decimal)-> str:
        """Decimal to string conversion """
        return  str(decimal_val)

    def int_enum_tostr(self, int_enum_val:IntEnum)-> str:
        """Int enum to string conversion """
        return  str(int_enum_val)

    def date_tostr(self, date_val: date) -> str:
        """date to string sconversion """
        return str(date_val)

    def time_tostr(self, time_val:time) -> str:
        """time to string conversion """
        return str(time_val)

    def str_toint(self, int_str: str) -> int:
        """String to int conversion """
        return int(int_str)

    def str_tofloat(self, float_str: str) -> float:
        """String to float conversion """
        return float(float_str)

    def str_todecimal(self, decimal_str: str) -> Decimal:
        """String to decimal conversion """
        return Decimal(decimal_str)

    def str_toenum(self, enum_type: Enum, enum_str: str) -> Enum:
        """String to enumeration conversion """
        return Enum.__getattribute__(enum_type,enum_str)

    # def str_tointenum(self, int_enum_str: str) -> IntEnum:
    #     return  IntEnum(int(int_enum_str))

    # def str_tostrenum(self, str_enum_val: str) -> StrEnum:
    #     return StrEnum(str_enum_val)

    def get_str_date_format(self,input_str: str)->str:
        """ Get string date format """
        matched_format: str = ''

        # \d{1,2}-\d{1,2}-\d{4} - dd-mm-yyyy
        # \d{4}-\d{1,2}-\d{1,2} - yyyy-mm-dd
        dd_mm_yyyy_or_yy_format:  regExp.Match[str] | None = None
        yyyy_or_yy_mm_dd_format: regExp.Match[str] | None = None

        dd_mm_yyyy_or_yy_format = regExp.match(
            '\\d{1,2}-\\d{1,2}-\\d{2,4}', input_str)

        yyyy_or_yy_mm_dd_format = regExp.match(
            '\\d{2,4}-\\d{1,2}-\\d{1,2}', input_str)

        if dd_mm_yyyy_or_yy_format is not None:
            matched_format = 'dd-mm-yyyy'
        elif yyyy_or_yy_mm_dd_format is not None:
            matched_format = 'yyyy-mm-dd'

        return matched_format

    def str_todate(self,date_str: str)-> date:
        """String to date conversion """
        year: int =0
        month: int = 0
        day: int = 0
        try:
            date_str_len = len(date_str)
            if date_str_len > 10:
                raise ValueError('Invalid date string.')
            date_format: str = self.get_str_date_format(date_str)
            date_str_pieces: list[str] = date_str.split('-')
            match date_format:
                case  'dd-mm-yyyy' | 'dd-mm-yy':
                    for str_piece in date_str_pieces:
                        int_piece =  int(str_piece)
                        len_str_piece: int = len(str_piece)
                        if day == 0:
                            if len_str_piece in (1,2) and int_piece in range(1,32):
                                day = int_piece
                        elif month == 0:
                            if len_str_piece in (1,2) and int_piece in range(1,13):
                                month = int_piece
                        elif year == 0:
                            if len_str_piece in (4,2) and int_piece in range(1,date.today().year +1):
                                year = int_piece
                case 'yyyy-mm-dd' | 'yy-mm-dd':
                    for str_piece in date_str_pieces:
                        int_piece =  int(str_piece)
                        len_str_piece: int = len(str_piece)
                        if year == 0:
                            if len_str_piece in (4,2) and int_piece in range(1,date.today().year+1):
                                year = int_piece
                        elif month == 0:
                            if len_str_piece in (1,2) and int_piece in range(1,13):
                                month = int_piece
                        elif day ==0:
                            if len_str_piece in (1,2) and int_piece in range(1,32):
                                day = int_piece
                case _: pass
        except SyntaxError as syntax_error:
            print(syntax_error)

        return date(year, month, day)

if __name__ == '__main__':
    py_type_instance =  PyTypeConverters()
    print(py_type_instance.str_todecimal('10.0'))
    result: Enum =  py_type_instance.str_toenum(Color, 'BLUE') # type: ignore
    print(result)
    print(py_type_instance.str_todate('12-10-2010'))
