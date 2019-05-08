

from ..utils import Object


class PushMessageContentChatJoinByLink(Object):
    """
    A new member joined the chat by invite link

    Attributes:
        ID (:obj:`str`): ``PushMessageContentChatJoinByLink``

    No parameters required.

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentChatJoinByLink"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatJoinByLink":
        
        return PushMessageContentChatJoinByLink()
