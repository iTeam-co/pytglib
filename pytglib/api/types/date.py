

from ..utils import Object


class Date(Object):
    """
    Represents a date according to the Gregorian calendar 

    Attributes:
        ID (:obj:`str`): ``Date``

    Args:
        day (:obj:`int`):
            Day of the month, 1-31 
        month (:obj:`int`):
            Month, 1-12 
        year (:obj:`int`):
            Year, 1-9999

    Returns:
        Date

    Raises:
        :class:`telegram.Error`
    """
    ID = "date"

    def __init__(self, day, month, year, **kwargs):
        
        self.day = day  # int
        self.month = month  # int
        self.year = year  # int

    @staticmethod
    def read(q: dict, *args) -> "Date":
        day = q.get('day')
        month = q.get('month')
        year = q.get('year')
        return Date(day, month, year)
