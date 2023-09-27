"""Module for Vehicle type enum """

from enum import Enum, _simple_enum, auto #type: ignore

@_simple_enum(Enum) #type: ignore
class VehicleTypes:
    """Vehicle types enumeration class"""
    Sedan = auto()
    Suv = auto()
    HatchBack = auto()
