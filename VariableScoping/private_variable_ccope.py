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
    _intVar: int = 0
    _strVar: str = ""

    def __init__(self) -> None:
        self._intVar = 1
        self._strVar = "Trial Class"
    
    def displayValues(self): 
        return  (self._intVar.__str__() + " " + self._strVar)

if __name__ == '__main__':
    obj = TrialClass()
    obj._intVar = 5
    obj._strVar = "No Private variable scoping in Python"

    print (obj.displayValues())