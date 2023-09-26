"""Module for Vehicle type enum """

from enum import Enum, _simple_enum, auto #type: ignore

@_simple_enum(Enum) #type: ignore
class VehicleTypes:
    Sedan = auto()
    Suv = auto()
    HatchBack = auto()
