"""Initializing py unit testing module"""
# from . import class_skipping
# from . import expected_failure_test
# from . import isolated_async_io_test
# from . import skipping_test_and_expected_failure
# from . import test_iteration_using_subtest
# from . import test_statistical_functions
# from . import unit_test_mock
# from . import widget_class

# __all__ = ['class_skipping', 'expected_failure_test', 'isolated_async_io_test',
#            'skipping_test_and_expected_failure', 'test_iteration_using_subtest',
#            'test_statistical_functions', 'unit_test_mock', 'widget_class']

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
