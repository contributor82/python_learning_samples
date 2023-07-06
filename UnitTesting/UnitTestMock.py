from unittest.mock import MagicMock, patch

class TempClass:
    intMember = 1
    strMember = ""

    def __init__(self):
        self.intMember = 1
        self.strMember = "Temp Class string member"

    def initial_data_values(self, newVal): 
        return self.intMember

    def change_data_values(self): 
        self.intMember = 5
        return self.intMember

    def display_values(self): 
        return self

# Used patch() decorator/context to make it easy to mock classes & objects. 

# Here what method call is expected
with patch.object(TempClass, 'initial_data_values', return_value=None) as mock_method:
     thing = TempClass()
     thing.initial_data_values(2)

# what is the actual mock call placed. Error when expected vs actual. 
mock_method.assert_called_once_with(1)




