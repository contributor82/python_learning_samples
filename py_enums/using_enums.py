"""Module for using class enumeration"""

from py_enums.color_enum import Color
from py_enums.vehicle_type_enum import VehicleTypes
from py_enums.string_enum import MessageTypes
from py_enums.int_enum import Numbers

class UsingEnums:
    """Module for using enumeration  """

    def using_color_enum(self)-> None:
        """Using color enum """
        for color_val in Color:
            print(color_val)

    def using_vehicle_type_enum(self)-> None:
        """using vehicle type enum """
        for vehicle_type in VehicleTypes: #type: ignore
            print(vehicle_type) #type: ignore


    def using_string_enum(self)-> None:
        """Using string enum """
        for message_type in MessageTypes: #type: ignore
            print(message_type) #type: ignore

    def using_int_enum(self)-> None:
        """Using integer enum """
        for num in Numbers: #type: ignore
            print(num) #type: ignore

if __name__ == '__main__':
    using_enums_instance = UsingEnums()
    using_enums_instance.using_color_enum()
    using_enums_instance.using_vehicle_type_enum()
    using_enums_instance.using_string_enum()
    using_enums_instance.using_int_enum()
