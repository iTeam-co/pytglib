

from ..utils import Object


class MessageSchedulingStateSendAtDate(Object):
    """
    The message will be sent at the specified date 

    Attributes:
        ID (:obj:`str`): ``MessageSchedulingStateSendAtDate``

    Args:
        send_date (:obj:`int`):
            Date the message will be sentThe date must be within 367 days in the future

    Returns:
        MessageSchedulingState

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSchedulingStateSendAtDate"

    def __init__(self, send_date, **kwargs):
        
        self.send_date = send_date  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageSchedulingStateSendAtDate":
        send_date = q.get('send_date')
        return MessageSchedulingStateSendAtDate(send_date)
