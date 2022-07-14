

from ..utils import Object


class UpdateChatPendingJoinRequests(Object):
    """
    The chat pending join requests were changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatPendingJoinRequests``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        pending_join_requests (:class:`telegram.api.types.chatJoinRequestsInfo`):
            The new data about pending join requests; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatPendingJoinRequests"

    def __init__(self, chat_id, pending_join_requests, **kwargs):
        
        self.chat_id = chat_id  # int
        self.pending_join_requests = pending_join_requests  # ChatJoinRequestsInfo

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatPendingJoinRequests":
        chat_id = q.get('chat_id')
        pending_join_requests = Object.read(q.get('pending_join_requests'))
        return UpdateChatPendingJoinRequests(chat_id, pending_join_requests)
