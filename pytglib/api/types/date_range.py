

from ..utils import Object


class DateRange(Object):
    """
    Represents a date range 

    Attributes:
        ID (:obj:`str`): ``DateRange``

    Args:
        start_date (:obj:`int`):
            Point in time (Unix timestamp) at which the date range begins 
        end_date (:obj:`int`):
            Point in time (Unix timestamp) at which the date range ends

    Returns:
        DateRange

    Raises:
        :class:`telegram.Error`
    """
    ID = "dateRange"

    def __init__(self, start_date, end_date, **kwargs):
        
        self.start_date = start_date  # int
        self.end_date = end_date  # int

    @staticmethod
    def read(q: dict, *args) -> "DateRange":
        start_date = q.get('start_date')
        end_date = q.get('end_date')
        return DateRange(start_date, end_date)
