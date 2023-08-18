"""Module for unit test magic mock """
from unittest.mock import MagicMock

class ProdClass:
    """Product class """
    num_list: list[int] = []

    def get_max(self, num1: int, num2: int , num3: int) -> int:
        """Get max of three numbers method """
        self.num_list.append(num1)
        self.num_list.append(num2)
        self.num_list.append(num3)
        return max(self.num_list)

    def get_min(self, num1: int, num2: int , num3: int) -> int:
        """Get max of three numbers method """
        self.num_list.append(num1)
        self.num_list.append(num2)
        self.num_list.append(num3)
        return min(self.num_list)

    def get_num_list(self) -> list[int]:
        """Get number list"""
        return self.num_list

if __name__ == '__main__':
    pc_instance = ProdClass()
    pc_instance.method = MagicMock(return_value=4) # type: ignore

    # MagicMock will mock the method call based on the number of arguments &
    # return value
    # assert called with given function arguments not matched then assertion error
    # will be thrown.
    pc_instance.method(3,4,2, key='value') # type: ignore
    pc_instance.method.assert_called_with(3,4,5,key='value') # type: ignore
