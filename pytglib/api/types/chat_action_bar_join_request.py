

from ..utils import Object


class ChatActionBarJoinRequest(Object):
    """
    The chat is a private chat with an administrator of a chat to which the user sent join request

    Attributes:
        ID (:obj:`str`): ``ChatActionBarJoinRequest``

    Args:
        title (:obj:`str`):
            Title of the chat to which the join request was sent
        is_channel (:obj:`bool`):
            True, if the join request was sent to a channel chat
        request_date (:obj:`int`):
            Point in time (Unix timestamp) when the join request was sent

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarJoinRequest"

    def __init__(self, title, is_channel, request_date, **kwargs):
        
        self.title = title  # str
        self.is_channel = is_channel  # bool
        self.request_date = request_date  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarJoinRequest":
        title = q.get('title')
        is_channel = q.get('is_channel')
        request_date = q.get('request_date')
        return ChatActionBarJoinRequest(title, is_channel, request_date)
