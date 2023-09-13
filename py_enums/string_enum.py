"""Module for Message types enum """

from enum import Enum, StrEnum, _simple_enum, auto #type: ignore

@_simple_enum(StrEnum) #type: ignore
class MessageTypes:
    """Message types enum"""
    Info = 'Information message. '
    Error = 'Error message'
    Warning = 'Warning message'
