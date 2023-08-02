from typing import Self
from unittest.mock import patch

class TempClass:
    intMember = 1
    strMember = ""

    def __init__(self) -> None:
        self.intMember = 1
        self.strMember = "Temp Class string member"

    def initial_data_values(self, newVal: int) -> int:
        self.intMember = newVal 
        return self.intMember

    def change_data_values(self) -> int: 
        self.intMember = 5
        return self.intMember

    def display_values(self) -> Self: 
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




