"""Module for testing class methods """
import unittest
import sys
sys.path.append('../Classes')
from bag_class_example import BagClass

class TestBagClass(unittest.TestCase):
    """Test bag class """
    bag_instance = BagClass()

    def test_bag_class_instance(self) -> None:
        """Test Bag class instance method """
        self.assertTrue(isinstance(self.bag_instance, BagClass)) #type: ignore

    def test_bag_class_add(self) -> None:
        """Test Bag class add method """
        self.bag_instance.add("First Element")
        self.assertTrue(len(self.bag_instance.data), 1)

    def test_bag_class_add_element_twice(self) -> None:
        """Test Bag class add element twice method """
        self.bag_instance.data.clear()
        self.bag_instance.add_element_twice("Element")
        self.assertTrue(len(self.bag_instance.data),2)

    def test_bag_class_whats_added_in_bag(self) -> None:
        """Test Bag class whats added in bag method """
        self.bag_instance.data.clear()
        self.bag_instance.add("One element")
        self.assertTrue(self.bag_instance.whats_added_in_bag(), ['One element'])

if __name__ == '__main__':
    unittest.main()

#python -m unittest test_class_methods -v
