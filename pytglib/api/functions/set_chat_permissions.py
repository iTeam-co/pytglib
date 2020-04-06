

from ..utils import Object


class SetChatPermissions(Object):
    """
    Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right

    Attributes:
        ID (:obj:`str`): ``SetChatPermissions``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        permissions (:class:`telegram.api.types.chatPermissions`):
            New non-administrator members permissions in the chat

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatPermissions"

    def __init__(self, chat_id, permissions, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.permissions = permissions  # ChatPermissions

    @staticmethod
    def read(q: dict, *args) -> "SetChatPermissions":
        chat_id = q.get('chat_id')
        permissions = Object.read(q.get('permissions'))
        return SetChatPermissions(chat_id, permissions)
