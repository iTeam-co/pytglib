

from ..utils import Object


class GetInactiveSupergroupChats(Object):
    """
    Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error

    Attributes:
        ID (:obj:`str`): ``GetInactiveSupergroupChats``

    No parameters required.

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getInactiveSupergroupChats"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetInactiveSupergroupChats":
        
        return GetInactiveSupergroupChats()
