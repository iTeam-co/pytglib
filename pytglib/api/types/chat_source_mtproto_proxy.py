

from ..utils import Object


class ChatSourceMtprotoProxy(Object):
    """
    The chat is sponsored by the user's MTProxy server

    Attributes:
        ID (:obj:`str`): ``ChatSourceMtprotoProxy``

    No parameters required.

    Returns:
        ChatSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatSourceMtprotoProxy"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatSourceMtprotoProxy":
        
        return ChatSourceMtprotoProxy()
