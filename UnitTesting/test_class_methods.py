# Following Import class statement is giving an error hence taken entire class
# for unit testing sample. 

# Importing BagClass from BagClassExample.py file

import sys
sys.path.append("\\Classes\\bag_class_example.py")

from ..Classes.bag_class_example import BagClass

import unittest

class TestBagClass(unittest.TestCase): 
    bag_instance = BagClass()

    def test_BagClass_Instance(self) -> None: 
        self.assertTrue(isinstance(self.bag_instance, BagClass))

    def test_BagClass_add(self): 
        self.bag_instance.add("First Element")
        self.assertTrue(self.bag_instance.data.__len__(), 1)
    
    def test_BagClass_add_element_twice(self) -> None:
         self.bag_instance.data.clear()
         self.bag_instance.add_element_twice("Element")
         self.assertTrue(self.bag_instance.data.__len__(),2)

    def test_BagClass_whats_added_in_bag(self) -> None: 
        self.bag_instance.data.clear()
        self.bag_instance.add("One element")
        self.assertTrue(self.bag_instance.whats_added_in_bag(), ['One element'])

if __name__ == '__main__': 
    unittest.main()


#python -m unittest test_class_methods -v