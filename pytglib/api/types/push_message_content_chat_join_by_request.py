

from ..utils import Object


class PushMessageContentChatJoinByRequest(Object):
    """
    A new member was accepted to the chat by an administrator

    Attributes:
        ID (:obj:`str`): ``PushMessageContentChatJoinByRequest``

    No parameters required.

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentChatJoinByRequest"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatJoinByRequest":
        
        return PushMessageContentChatJoinByRequest()
