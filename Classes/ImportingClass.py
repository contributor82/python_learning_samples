# Class impported from same folder. 
from BagClassExample import BagClass

bagInstance = BagClass()

bagInstance.add('Compass Box')
bagInstance.add_element_twice('Book')
bagInstance.add_element_twice('Book')
bagInstance.add_element_twice('Note Book')
bagInstance.add_element_twice('Note Book')
bagInstance.add('Water Bottle')
bagInstance.add('Lunch Box')
bagInstance.add('Raincoat with bag')


bagElements = bagInstance.whats_added_in_bag()

print('What is in your Bag:', bagElements)

