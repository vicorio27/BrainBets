"""
Player Model
"""


class Player:
    """
    Payer
    """

    def __init__(self, **kwargs):
        """
        Constructor.

        """
        self.__dict__ = kwargs

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "id", self.id
        yield "name", self.name
        yield "age", self.age
        yield "genre", self.genre
        yield "nacionality", self.nationality
        yield "set1", self.set1
        yield "set2", self.set2
        yield "set3", self.set3
        yield "association", self.association
        yield "winornot1", self.winornot1
