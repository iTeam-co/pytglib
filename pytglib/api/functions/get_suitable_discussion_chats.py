

from ..utils import Object


class GetSuitableDiscussionChats(Object):
    """
    Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first

    Attributes:
        ID (:obj:`str`): ``GetSuitableDiscussionChats``

    No parameters required.

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSuitableDiscussionChats"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetSuitableDiscussionChats":
        
        return GetSuitableDiscussionChats()
