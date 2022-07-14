

from ..utils import Object


class ReplacePrimaryChatInviteLink(Object):
    """
    Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right 

    Attributes:
        ID (:obj:`str`): ``ReplacePrimaryChatInviteLink``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        ChatInviteLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "replacePrimaryChatInviteLink"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ReplacePrimaryChatInviteLink":
        chat_id = q.get('chat_id')
        return ReplacePrimaryChatInviteLink(chat_id)
