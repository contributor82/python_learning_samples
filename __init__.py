"""Module initialization"""
# from . import py_class_creation
# from . import py_comprehensions
# from . import py_data_operations
# from . import py_data_structures
# from . import py_email_funcs
# from . import py_examples
# from . import py_file_operations
# from . import py_inheritance
# from . import py_json_encoders
# from . import py_logging_funcs
# from . import py_misc
# from . import py_modules
# from . import py_patterns
# from . import py_perf_funcs
# from . import py_string_operations
# from . import py_threading_funcs
# from . import py_unit_testing

# __all__ = ['py_class_creation', 'py_comprehensions', 'py_data_operations',
#            'py_data_structures', 'py_email_funcs', 'py_examples', 'py_file_operations',
#            'py_inheritance', 'py_json_encoders', 'py_logging_funcs', 'py_misc', 'py_modules',
#            'py_patterns', 'py_perf_funcs', 'py_string_operations', 'py_threading_funcs',
#            'py_unit_testing']

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
