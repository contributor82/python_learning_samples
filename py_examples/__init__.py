"""Initializing examples module """
# from . import bag_class
# from . import get_your_age
# from . import product_class
# from . import product_funcs

# __all__ = ['bag_class', 'get_your_age', 'product_class', 'product_funcs']

from pkgutil import extend_path
# this works for python modules present in the same directory.
__path__ = extend_path(__path__, __name__)
