

from ..utils import Object


class GetChatJoinRequests(Object):
    """
    Returns pending join requests in a chat

    Attributes:
        ID (:obj:`str`): ``GetChatJoinRequests``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        invite_link (:obj:`str`):
            Invite link for which to return join requestsIf empty, all join requests will be returnedRequires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        query (:obj:`str`):
            A query to search for in the first names, last names and usernames of the users to return
        offset_request (:class:`telegram.api.types.chatJoinRequest`):
            A chat join request from which to return next requests; pass null to get results from the beginning
        limit (:obj:`int`):
            The maximum number of requests to join the chat to return

    Returns:
        ChatJoinRequests

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatJoinRequests"

    def __init__(self, chat_id, invite_link, query, offset_request, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.invite_link = invite_link  # str
        self.query = query  # str
        self.offset_request = offset_request  # ChatJoinRequest
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatJoinRequests":
        chat_id = q.get('chat_id')
        invite_link = q.get('invite_link')
        query = q.get('query')
        offset_request = Object.read(q.get('offset_request'))
        limit = q.get('limit')
        return GetChatJoinRequests(chat_id, invite_link, query, offset_request, limit)
