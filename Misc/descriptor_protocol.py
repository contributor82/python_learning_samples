# """Module for descriptor protocol """

# # DO NOT USE, currently throwing an error.
# class int_field:
#     """Int field class """
#     name: str = ''

#     def __get__(self, instance, owner):
#         """Get method """
#         return instance.__dict__[self.name]

#     def __set__(self,instance, value):
#         """Set method """
#         if not isinstance(value, int):
#             raise ValueError(f"Expecting integer in {self.name}")
#         instance.__dict__[self.name] = value

#     def __set__name(self, instance, name):
#         """Set name method """
#         self.name = name


# if __name__ == '__main__':
#     # class Model:
#     int_field = int_field()
#     int_field.__set__name("Int Field")
