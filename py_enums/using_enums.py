"""Module for using class enumeration"""
from color_enum import Color #type: ignore
from vehicle_type_enum import VehicleTypes #type: ignore
from string_enum import MessageTypes #type: ignore
from int_enum import Numbers #type: ignore

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
