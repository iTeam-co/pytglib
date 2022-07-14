

from ..utils import Object


class ChatJoinRequestsInfo(Object):
    """
    Contains information about pending join requests for a chat 

    Attributes:
        ID (:obj:`str`): ``ChatJoinRequestsInfo``

    Args:
        total_count (:obj:`int`):
            Total number of pending join requests 
        user_ids (List of :obj:`int`):
            Identifiers of at most 3 users sent the newest pending join requests

    Returns:
        ChatJoinRequestsInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatJoinRequestsInfo"

    def __init__(self, total_count, user_ids, **kwargs):
        
        self.total_count = total_count  # int
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ChatJoinRequestsInfo":
        total_count = q.get('total_count')
        user_ids = q.get('user_ids')
        return ChatJoinRequestsInfo(total_count, user_ids)
