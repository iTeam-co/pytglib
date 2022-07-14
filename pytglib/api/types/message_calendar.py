

from ..utils import Object


class MessageCalendar(Object):
    """
    Contains information about found messages, split by days according to the option "utc_time_offset" 

    Attributes:
        ID (:obj:`str`): ``MessageCalendar``

    Args:
        total_count (:obj:`int`):
            Total number of found messages 
        days (List of :class:`telegram.api.types.messageCalendarDay`):
            Information about messages sent

    Returns:
        MessageCalendar

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageCalendar"

    def __init__(self, total_count, days, **kwargs):
        
        self.total_count = total_count  # int
        self.days = days  # list of messageCalendarDay

    @staticmethod
    def read(q: dict, *args) -> "MessageCalendar":
        total_count = q.get('total_count')
        days = [Object.read(i) for i in q.get('days', [])]
        return MessageCalendar(total_count, days)
