"""Module for director class"""

from base_product import BaseProduct
from builder_class import  BuilderProductClass
from derived_product_one import DerivedProductOne
from derived_product_two import DerivedProductTwo

class DirectorClass:
    """Class for director"""
    builder_product_class: BuilderProductClass
    product_request: BaseProduct
    director_instance: object = None

    # def __init__(self, builder_product: BuilderProductClass, prod_req:BaseProduct) -> None:
    #     """Initializing client one class"""
    #     self.builder_class = builder_product
    #     self.product_request = prod_req

    def __new__(cls, builder_product: BuilderProductClass, prod_req:BaseProduct) -> object:
        return_director_obj = None
        """Director class instance """
        if cls.director_instance is None:
            cls.director_instance = super().__new__(cls)
            cls.builder_class = builder_product
            cls.product_request = prod_req

        return_director_obj = cls.director_instance
        return return_director_obj

    def build_product(self)-> None:
        """Build Product """
        if type(self.product_request) is DerivedProductOne:
            # do something
            self.builder_class.int_member = 1
            self.builder_class.str_member = 'Derived one'
            self.builder_class.build_product()
        elif type(self.product_request) is DerivedProductTwo:
            # do something
            self.builder_class.int_member = 2
            self.builder_class.str_member = 'Derived two'
            self.builder_class.build_product()
        else:
            # "Nothing to  do"
            print('No complex object building since not requested.')


    def get_product(self) -> BaseProduct | None:
        """Get product """
        return self.builder_class.get_product()
