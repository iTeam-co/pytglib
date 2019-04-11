

from ..utils import Object


class MessageChatDeletePhoto(Object):
    """
    A deleted chat photo

    Attributes:
        ID (:obj:`str`): ``MessageChatDeletePhoto``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatDeletePhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageChatDeletePhoto":
        
        return MessageChatDeletePhoto()
