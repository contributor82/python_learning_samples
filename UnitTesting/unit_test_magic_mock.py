from unittest.mock import MagicMock

class ProdClass:

    # Returns max of three numbers. 
    def get_max(self, num1: int, num2: int , num3: int): 
        num_list = [int]
        num_list.insert(num1)
        num_list.insert(num2)
        num_list.insert(num3)
        return max(num_list)
    

if __name__ == '__main__': 
    pc_instance = ProdClass()
    pc_instance.method = MagicMock(return_value=4)

    # MagicMock will mock the method call based on the number of arguments & 
    # return value
    # assert called with given function arguments not matched then assertion error
    # will be thrown. 
    pc_instance.method(3,4,2, key='value')
    pc_instance.method.assert_called_with(3,4,5,key='value')

        
        

