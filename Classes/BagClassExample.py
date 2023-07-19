# An example using class to add elements in Bag collection
# Returning Bag elements. 
import sys

class BagClass: 

    def __init__(self) -> None:
        self.data = ['']

    def add(self, element: str) -> None:
        self.data.append(element)
    
    def add_element_twice(self, element: str) -> None: 
        self.data.append(element)
        self.data.append(element)

    def whats_added_in_bag(self) -> list[str]: 
        return self.data
        

if __name__ == '__main__': 
        # print("In module TestClassMethods __package__ and __name__ : ", __package__, __name__)
        # print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)

# Commented since class has been invoked from another file. 
    bagObject = BagClass()
    bagObject.add("Compass box")
    bagObject.add_element_twice("Book")
    bagObject.add_element_twice("Notebook")
    print("What is added in the bag: ", bagObject.whats_added_in_bag())




