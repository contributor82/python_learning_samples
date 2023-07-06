# An example using class to add elements in Bag collection
# Returning Bag elements. 

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
        
# Commented since class has been invoked from another file. 
# bagObject = BagClass()
# bagObject.add("Compass box")
# bagObject.add_element_twice("Book")
# bagObject.add_element_twice("Notebook")
# print("What is added in the bag: ", bagObject.whats_added_in_bag())




