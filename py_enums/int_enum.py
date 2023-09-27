"""Module for Message types enum """

from enum import IntEnum, _simple_enum #type: ignore

@_simple_enum(IntEnum) #type: ignore
class Numbers:
    """Numbers enumeration class """
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
