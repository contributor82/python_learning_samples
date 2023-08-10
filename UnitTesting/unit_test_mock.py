"""Module for unit test mock """
from typing import Self
from unittest.mock import patch

class TempClass:
    """Temp class """

    int_member: int = 1
    str_member: str = ""

    def __init__(self) -> None:
        """Initializing class members """
        self.int_member = 1
        self.str_member = "Temp Class string member"

    def initial_data_values(self, new_val: int) -> int:
        """Setting initial data values method """
        self.int_member = new_val
        return self.int_member

    def change_data_values(self) -> int:
        """Chnaging data values method """
        self.int_member = 5
        return self.int_member

    def display_values(self) -> Self:
        """Returning display values """
        return self

# Used patch() decorator/context to make it easy to mock classes & objects.

if __name__ == '__main__':

# Here what method call is expected
# Patch will use TempClass instance and call method passed as "mock_method"
# The expected result will match only when passed value and function name matches.
    with patch.object(TempClass, 'initial_data_values', return_value=None) as mock_method:
        thing = TempClass()
        thing.initial_data_values(2)

    # Here mock_method is holding TempClass instance and calling initial_data_values as its method.
    # Error when expected vs actual.
    mock_method.assert_called_once_with(1)
