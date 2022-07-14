

from ..utils import Object


class ChatJoinRequests(Object):
    """
    Contains a list of requests to join a chat 

    Attributes:
        ID (:obj:`str`): ``ChatJoinRequests``

    Args:
        total_count (:obj:`int`):
            Approximate total number of requests found 
        requests (List of :class:`telegram.api.types.chatJoinRequest`):
            List of the requests

    Returns:
        ChatJoinRequests

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatJoinRequests"

    def __init__(self, total_count, requests, **kwargs):
        
        self.total_count = total_count  # int
        self.requests = requests  # list of chatJoinRequest

    @staticmethod
    def read(q: dict, *args) -> "ChatJoinRequests":
        total_count = q.get('total_count')
        requests = [Object.read(i) for i in q.get('requests', [])]
        return ChatJoinRequests(total_count, requests)
