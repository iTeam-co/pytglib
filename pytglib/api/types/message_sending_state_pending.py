

from ..utils import Object


class MessageSendingStatePending(Object):
    """
    The message is being sent now, but has not yet been delivered to the server

    Attributes:
        ID (:obj:`str`): ``MessageSendingStatePending``

    No parameters required.

    Returns:
        MessageSendingState

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSendingStatePending"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageSendingStatePending":
        
        return MessageSendingStatePending()
