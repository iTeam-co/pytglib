

from ..utils import Object


class MessageChatJoinByLink(Object):
    """
    A new member joined the chat by invite link

    Attributes:
        ID (:obj:`str`): ``MessageChatJoinByLink``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatJoinByLink"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageChatJoinByLink":
        
        return MessageChatJoinByLink()
