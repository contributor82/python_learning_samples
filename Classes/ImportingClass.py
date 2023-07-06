from BagClassExample import BagClass

bagObj = BagClass()

bagObj.add('Compass Box')
bagObj.add_element_twice('Book')
bagObj.add_element_twice('Book')
bagObj.add_element_twice('Note Book')
bagObj.add_element_twice('Note Book')
bagObj.add('Water Bottle')
bagObj.add('Lunch Box')
bagObj.add('Raincoat with bag')


bagElements = bagObj.whats_added_in_bag()

print('What is in your Bag:', bagElements)

