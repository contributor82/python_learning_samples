"""Module for Message types enum """

from enum import Enum, IntEnum, _simple_enum, auto #type: ignore

@_simple_enum(IntEnum) #type: ignore
class Numbers:
    One = 1,
    Two = 2,
    Three = 3,
    Four = 4,
    Five = 5


