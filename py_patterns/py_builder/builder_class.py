"""Module for Builder class """

from base_product import BaseProduct
from derived_product_one import DerivedProductOne
from derived_product_two import DerivedProductTwo

class BuilderProductClass:
    """Builder product class """
    int_member: int = 0
    str_member: str = ""
    product: BaseProduct | None

    def build_product(self)-> None:
        """Build Product """
        if self.int_member == 1:
            self.product = DerivedProductOne()
            self.product.derived_one_int_member = self.int_member
            self.product.derived_one_str_member = self.str_member
        elif self.int_member == 2:
            self.product = DerivedProductTwo()
            self.product.derived_two_int_member = self.int_member
            self.product.derived_two_str_member = self.str_member
        else:
            self.product = None

    def get_product(self) -> BaseProduct | None:
        """Get product """
        return self.product
