

from ..utils import Object


class MessageSchedulingStateSendWhenOnline(Object):
    """
    The message will be sent when the peer will be online. Applicable to private chats only and when the exact online status of the peer is known

    Attributes:
        ID (:obj:`str`): ``MessageSchedulingStateSendWhenOnline``

    No parameters required.

    Returns:
        MessageSchedulingState

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSchedulingStateSendWhenOnline"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageSchedulingStateSendWhenOnline":
        
        return MessageSchedulingStateSendWhenOnline()
