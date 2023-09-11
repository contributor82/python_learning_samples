"""Module for client one class"""

from base_product import BaseProduct
from builder_class import BuilderProductClass
from derived_product_one import DerivedProductOne #type: ignore
from director_class import DirectorClass
from derived_product_two import DerivedProductTwo #type: ignore


class ClientOneClass:
    """Client One class"""
    director_class: DirectorClass

    def __init__(self) -> None:
        """Initializing Client one class """
        self.director_class =  DirectorClass(BuilderProductClass(), DerivedProductTwo())


    def develop_product(self)-> None:
        """Develop product """
        self.director_class.build_product()

    def get_product_outcome(self)->None:
        """Get product outcome """
        result: BaseProduct | None = self.director_class.get_product()
        print("int: ", result.derived_two_int_member, " string: ", result.derived_two_str_member) #type: ignore
        # print("Result : ", result.int_member)


if __name__ == '__main__':
    client_one_instance = ClientOneClass()
    client_one_instance.develop_product()
    client_one_instance.get_product_outcome()
