from typing import TypeVar, Generic, Optional

"""
Event
"""

T = TypeVar("T")

class Response(Generic[T]):
    success: int
    result: list[T]

    def __init__(self, event_type_key: str, event_type_type: str):
        """
        Constructor.
        """
        self.event_type_key = event_type_key
        self.event_type_type = event_type_type
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "event_type_key", self.event_type_key
        yield "event_type_type", self.event_type_type
