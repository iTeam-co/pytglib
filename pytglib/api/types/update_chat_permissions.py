

from ..utils import Object


class UpdateChatPermissions(Object):
    """
    Chat permissions was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatPermissions``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        permissions (:class:`telegram.api.types.chatPermissions`):
            The new chat permissions

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatPermissions"

    def __init__(self, chat_id, permissions, **kwargs):
        
        self.chat_id = chat_id  # int
        self.permissions = permissions  # ChatPermissions

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatPermissions":
        chat_id = q.get('chat_id')
        permissions = Object.read(q.get('permissions'))
        return UpdateChatPermissions(chat_id, permissions)
