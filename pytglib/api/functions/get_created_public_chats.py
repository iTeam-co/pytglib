

from ..utils import Object


class GetCreatedPublicChats(Object):
    """
    Returns a list of public chats created by the user

    Attributes:
        ID (:obj:`str`): ``GetCreatedPublicChats``

    No parameters required.

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCreatedPublicChats"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetCreatedPublicChats":
        
        return GetCreatedPublicChats()
