

from ..utils import Object


class MessageSendingStateFailed(Object):
    """
    The message failed to be sent

    Attributes:
        ID (:obj:`str`): ``MessageSendingStateFailed``

    No parameters required.

    Returns:
        MessageSendingState

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSendingStateFailed"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageSendingStateFailed":
        
        return MessageSendingStateFailed()
