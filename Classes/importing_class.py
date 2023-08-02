# Class impported from same folder. 
from bag_class_example import BagClass

bag_instance = BagClass()

bag_instance.add('Compass Box')
bag_instance.add_element_twice('Book')
bag_instance.add_element_twice('Book')
bag_instance.add_element_twice('Note Book')
bag_instance.add_element_twice('Note Book')
bag_instance.add('Water Bottle')
bag_instance.add('Lunch Box')
bag_instance.add('Raincoat with bag')


bag_elements: list[str] = bag_instance.whats_added_in_bag()

print('What is in your Bag:', bag_elements)

