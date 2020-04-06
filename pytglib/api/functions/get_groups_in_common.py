

from ..utils import Object


class GetGroupsInCommon(Object):
    """
    Returns a list of common group chats with a given user. Chats are sorted by their type and creation date 

    Attributes:
        ID (:obj:`str`): ``GetGroupsInCommon``

    Args:
        user_id (:obj:`int`):
            User identifier 
        offset_chat_id (:obj:`int`):
            Chat identifier starting from which to return chats; use 0 for the first request 
        limit (:obj:`int`):
            The maximum number of chats to be returned; up to 100

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getGroupsInCommon"

    def __init__(self, user_id, offset_chat_id, limit, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.offset_chat_id = offset_chat_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetGroupsInCommon":
        user_id = q.get('user_id')
        offset_chat_id = q.get('offset_chat_id')
        limit = q.get('limit')
        return GetGroupsInCommon(user_id, offset_chat_id, limit)
