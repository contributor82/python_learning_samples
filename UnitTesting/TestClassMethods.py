# Following Import class statement is giving an error hence taken entire class
# for unit testing sample. 

# Importing BagClass from BagClassExample.py file

import sys
sys.path.append(r"\Classes")

from BagClassExample import BagClass

# Following import statement doesn't work. 
#from ..Classes.BagClassExample import BagClass

import unittest

class TestBagClass(unittest.TestCase): 
    bagInstance = BagClass()

    def test_BagClass_Instance(self) -> None: 
        self.assertTrue(isinstance(self.bagInstance, BagClass))

    def test_BagClass_add(self): 
        self.bagInstance.add("First Element")
        self.assertTrue(self.bagInstance.data.__len__(), 1)
    
    def test_BagClass_add_element_twice(self) -> None:
         self.bagInstance.data.clear()
         self.bagInstance.add_element_twice("Element")
         self.assertTrue(self.bagInstance.data.__len__(),2)

    def test_BagClass_whats_added_in_bag(self) -> None: 
        self.bagInstance.data.clear()
        self.bagInstance.add("One element")
        self.assertTrue(self.bagInstance.whats_added_in_bag(), ['One element'])

if __name__ == '__main__': 
    unittest.main()


#python -m unittest TestClassMethods -v