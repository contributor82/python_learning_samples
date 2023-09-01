"""Test module for module load"""
import sys
import unittest
import importlib
from types import ModuleType

class TestModuleLoad(unittest.TestCase):
    """Test Module Load class"""

    def test_module_load_using_import(self)-> None:
        """Test module load using import """
        try:
            imported_module: ModuleType =  importlib.import_module('product_class', 'py_examples')
            self.assertEqual('product_class', imported_module.__name__)
            print('test_module_load_using_import success')
        except ModuleNotFoundError as module_not_error:
            self.assertTrue(module_not_error, ModuleNotFoundError)

    def test_module_load_using_get(self)-> None:
        """Test module load using get """
        try:
            sys_imported_module: ModuleType | None =  sys.modules.get(
                'py_class_creation') # type: ignore
            if not sys_imported_module is None:
                self.assertEqual('product_class', sys_imported_module.__name__)
            else:
                self.assertEqual('product_class', None)
            print('test_module_load_using_get success')
        except ModuleNotFoundError as sys_module_not_error:
            self.assertTrue(sys_module_not_error, ModuleNotFoundError)
        except AssertionError as sys_assertion_error:
            self.assertTrue(sys_assertion_error, AssertionError)

if __name__ == '__main__':
    unittest.main()

# python -m unittest test_module_load -v
