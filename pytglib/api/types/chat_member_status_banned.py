

from ..utils import Object


class ChatMemberStatusBanned(Object):
    """
    The user or the chat was banned (and hence is not a member of the chat). Implies the user can't return to the chat, view messages, or be used as a participant identifier to join a video chat of the chat

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusBanned``

    Args:
        banned_until_date (:obj:`int`):
            Point in time (Unix timestamp) when the user will be unbanned; 0 if neverIf the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned foreverAlways 0 in basic groups

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusBanned"

    def __init__(self, banned_until_date, **kwargs):
        
        self.banned_until_date = banned_until_date  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusBanned":
        banned_until_date = q.get('banned_until_date')
        return ChatMemberStatusBanned(banned_until_date)
