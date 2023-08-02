# class Mapping: 

#     def __init__(self,  iterable):
#         self.item_list = []
#         self._update(iterable)
    
#     def update(self, iterable): 
#         for item in iterable: 
#             self.item_list.append(item)
    
#     _update = update

# class MappingSubClass(Mapping): 

#     def update(self, keys, values): 
#         for item in zip(keys, values): 
#             self.item_list.append(item)

# elements = [1,2,3]

# obj = MappingSubClass(elements)
# obj.update("B", "I")
# obj.update("A", "B")

# print(obj.item_list)


class TrialClass: 
    _int_var: int = 0
    _str_var: str = ""

    def __init__(self) -> None:
        self._int_var = 1
        self._str_var = "Trial Class"
    
    def displayValues(self): 
        return  (self._int_var.__str__() + " " + self._str_var)

if __name__ == '__main__':
    obj = TrialClass()
    obj._int_var = 5
    obj._str_var = "No Private variable scoping in Python"

    print (obj.displayValues())