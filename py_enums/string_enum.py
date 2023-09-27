"""Module for Message types enum """
from enum import StrEnum, _simple_enum #type: ignore

@_simple_enum(StrEnum) #type: ignore
class MessageTypes:
    """Message types enumeration class"""
    Info = 'Information message. '
    Error = 'Error message'
    Warning = 'Warning message'
