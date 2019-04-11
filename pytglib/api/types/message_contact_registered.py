

from ..utils import Object


class MessageContactRegistered(Object):
    """
    A contact has registered with Telegram

    Attributes:
        ID (:obj:`str`): ``MessageContactRegistered``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageContactRegistered"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageContactRegistered":
        
        return MessageContactRegistered()
