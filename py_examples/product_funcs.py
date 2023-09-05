"""Module for Product functions """
import csv
from argparse import ArgumentError
from .product_class import Product

class ProductFuncs:
    """Product functions """
    product_list: list[Product]

    def __init__(self) -> None:
        """Initializing product list"""
        self.product_list = [Product()]

    def load_products(self, csv_file_name: str) -> None:
        """Load products method """
        try:
            with open(csv_file_name, encoding='utf-8',mode='r') as csv_file_handle:
                csv_dict_reader = csv.DictReader(csv_file_handle)
                for row in csv_dict_reader:
                    product_instance = Product()
                    product_instance.product_id = int(row['product_id'])
                    product_instance.name = row['name']
                    product_instance.unit_price = float(row['unit_price'])
                    product_instance.quantity = int(row['quantity'])
                    self.product_list.append(product_instance)
        except ArgumentError as argument_error:
            print(argument_error)
        except KeyError as key_error:
            print(key_error)
        except FileNotFoundError as csv_file_not_found_error:
            print(csv_file_not_found_error)
        except OSError as os_error:
            print(os_error)

    def display_products_with_calculated_stock_price(self) -> None:
        """Display products with calculated stock price """
        try:
            calc_price: float = 0.0
            for prod in self.product_list:
                calc_price = prod.quantity * prod.unit_price
                print('Product ID: ', prod.product_id,  'name: ', prod.name,
                    ' Unit price: ', prod.unit_price, ' Qty: ', prod.quantity,
                    ' Stock price: ', calc_price)
                calc_price = 0.0
        except ValueError as value_error:
            print(value_error)
        except TypeError as type_error:
            print(type_error)


    def find_product_by_name(self, product_name:str) -> Product | None:
        """Find product by name method """
        found_product: Product | None = None
        try:
            for prod in self.product_list:
                if prod.name == product_name:
                    found_product = prod
                    break
        except ValueError as value_error:
            print(value_error)
        except TypeError as type_error:
            print(type_error)
        return found_product

if __name__ == '__main__':
    product_funcs_instance = ProductFuncs()
    product_funcs_instance.load_products('C:\\Data\\products.csv')
    product_funcs_instance.display_products_with_calculated_stock_price()
    product: Product | None =  product_funcs_instance.find_product_by_name(
        'Product two')

    if not product is None:
        product.display_product_dtls()
