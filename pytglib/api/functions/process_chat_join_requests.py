

from ..utils import Object


class ProcessChatJoinRequests(Object):
    """
    Handles all pending join requests for a given link in a chat

    Attributes:
        ID (:obj:`str`): ``ProcessChatJoinRequests``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        invite_link (:obj:`str`):
            Invite link for which to process join requestsIf empty, all join requests will be processedRequires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        approve (:obj:`bool`):
            Pass true to approve all requests; pass false to decline them

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "processChatJoinRequests"

    def __init__(self, chat_id, invite_link, approve, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.invite_link = invite_link  # str
        self.approve = approve  # bool

    @staticmethod
    def read(q: dict, *args) -> "ProcessChatJoinRequests":
        chat_id = q.get('chat_id')
        invite_link = q.get('invite_link')
        approve = q.get('approve')
        return ProcessChatJoinRequests(chat_id, invite_link, approve)
