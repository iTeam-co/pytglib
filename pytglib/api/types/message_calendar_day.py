

from ..utils import Object


class MessageCalendarDay(Object):
    """
    Contains information about found messages sent on a specific day 

    Attributes:
        ID (:obj:`str`): ``MessageCalendarDay``

    Args:
        total_count (:obj:`int`):
            Total number of found messages sent on the day 
        message (:class:`telegram.api.types.message`):
            First message sent on the day

    Returns:
        MessageCalendarDay

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageCalendarDay"

    def __init__(self, total_count, message, **kwargs):
        
        self.total_count = total_count  # int
        self.message = message  # Message

    @staticmethod
    def read(q: dict, *args) -> "MessageCalendarDay":
        total_count = q.get('total_count')
        message = Object.read(q.get('message'))
        return MessageCalendarDay(total_count, message)
