"""Module for private variable scoping """
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
    """Trail class """
    int_var: int = 0
    str_var: str = ""

    def __init__(self) -> None:
        """Initializing class members """
        self.int_var = 1
        self.str_var = "Trial Class"

    def update_values(self, int_val: int, str_val: str)-> None:
        """Updating class members """
        self.int_var = int_val
        self.str_var = str_val

    def display_values(self) -> str:
        """ Displaying values method """
        return  str(self.int_var) + " " + self.str_var


if __name__ == '__main__':
    obj = TrialClass()
    obj.update_values(5, "No Private variable scoping in Python")
    print (obj.display_values())
