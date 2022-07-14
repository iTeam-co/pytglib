

from ..utils import Object


class GetChatInviteLinkCounts(Object):
    """
    Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat 

    Attributes:
        ID (:obj:`str`): ``GetChatInviteLinkCounts``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        ChatInviteLinkCounts

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatInviteLinkCounts"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatInviteLinkCounts":
        chat_id = q.get('chat_id')
        return GetChatInviteLinkCounts(chat_id)
