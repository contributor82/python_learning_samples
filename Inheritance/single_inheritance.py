
"""Module for Single inheritance in Python"""
# Base Class added with members and display method.
class Apartment:
    """ Base class """
    num_of_rooms: int
    sqft_area: float
    num_of_bath_rooms: int
    str_base_member: str = "Apartment Base Class"

    def __init__(self) -> None:
        self.num_of_rooms = 0
        self.sqft_area = 0
        self.num_of_bath_rooms =0

    def get_str_base_member(self) -> str:
        """ Display base class string member """
        return self.str_base_member

    def get_num_of_rooms(self)-> int:
        """ Get int base member """
        return self.num_of_rooms

    def get_num_of_bath_rooms(self)-> int:
        """ Get num of bathrooms """
        return self.num_of_bath_rooms

    def display_apartment(self)-> None:
        """Display base members """
        print("Rooms : ", self.num_of_rooms,
              "Area: ", self.sqft_area,
              "Bath rooms: ", self.num_of_bath_rooms,
              "Name : ", self.str_base_member)


class TwoBedApartment(Apartment):
    """ Derived class """
    duplex: bool
    str_derived_member: str = "Two bed apartment Derived Class"

    def get_str_derived_member(self) -> str:
        """ Display derived class string member """
        return self.str_derived_member

    def get_duplex(self)-> bool:
        """ Get duplex """
        return self.duplex

    def display_derived(self) -> None:
        """ Displaying derived class string member """
        print(" Is duplex : ", self.duplex, " Name: ", self.str_derived_member)

if __name__ == '__main__':
    # Derived Class instance created.
    two_bed_apt_instance = TwoBedApartment()

    # Invoked Base class method
    print("Base Class method invocation: ")
    two_bed_apt_instance.display_apartment()

    # Invoked Derived class method.
    print("Derived Class method invocation: ")
    two_bed_apt_instance.display_derived()
