

from ..utils import Object


class MessageChatJoinByRequest(Object):
    """
    A new member was accepted to the chat by an administrator

    Attributes:
        ID (:obj:`str`): ``MessageChatJoinByRequest``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatJoinByRequest"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageChatJoinByRequest":
        
        return MessageChatJoinByRequest()
