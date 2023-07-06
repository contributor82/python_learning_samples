# Following Import class statement is giving an error hence taken entire class
# for unit testing sample. 
# from ..Classes.BagClassExample import BagClass
import unittest

class BagClass: 

    def __init__(self):
        self.data = []

    def add(self, element):
        self.data.append(element)
    
    def add_element_twice(self, element): 
        self.data.append(element)
        self.data.append(element)

    def whats_added_in_bag(self): 
        return self.data


class TestBagClass(unittest.TestCase): 
    bagObj = BagClass()
    def test_BagClass_Instance(self): 
        self.assertTrue(isinstance(self.bagObj, BagClass))

    def test_BagClass_add(self): 
        self.bagObj.add("First Element")
        self.assertTrue(self.bagObj.data.__len__(), 1)
    
    def test_BagClass_add_element_twice(self):
         self.bagObj.data.clear()
         self.bagObj.add_element_twice("Element")
         self.assertTrue(self.bagObj.data.__len__(),2)

    def test_BagClass_whats_added_in_bag(self): 
        self.bagObj.data.clear()
        self.bagObj.add("One element")
        self.assertTrue(self.bagObj.whats_added_in_bag(), ['One element'])

if __name__ == '__main__': 
    unittest.main()
