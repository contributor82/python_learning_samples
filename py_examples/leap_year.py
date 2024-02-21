"""Module for leap year check """


class LeapYearCheck:
    """Leap year check class """
    input_year: int

    def __init__(self, ip_year: int) -> None:
        """Initialize defaults """
        self.input_year = ip_year

    def check_for_leap_year(self) -> bool:
        """Check for leap year"""
        is_leap_year: bool = False
        # divided by 100 means century year (ending with 00)
        # century year divided by 400 is leap year
        if (self.input_year % 400 == 0) & (self.input_year % 100 == 0):
            is_leap_year = True

        # not divided by 100 means not a century year
        # year divided by 4 is a leap year
        elif (self.input_year % 4 == 0) & (self.input_year % 100 != 0):
            is_leap_year = True
        else:
            is_leap_year = False

        return is_leap_year


if __name__ == '__main__':
    input_year = int(input('Enter year : '))
    leap_yr_check_instance = LeapYearCheck(input_year)
    is_leap_year: bool = leap_yr_check_instance.check_for_leap_year()

    if is_leap_year == True:
        print(f'{input_year} is a leap year')
    else:
        print(f'{input_year} is not a leap year')
