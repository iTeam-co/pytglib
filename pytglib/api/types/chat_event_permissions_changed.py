

from ..utils import Object


class ChatEventPermissionsChanged(Object):
    """
    The chat permissions was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventPermissionsChanged``

    Args:
        old_permissions (:class:`telegram.api.types.chatPermissions`):
            Previous chat permissions 
        new_permissions (:class:`telegram.api.types.chatPermissions`):
            New chat permissions

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventPermissionsChanged"

    def __init__(self, old_permissions, new_permissions, **kwargs):
        
        self.old_permissions = old_permissions  # ChatPermissions
        self.new_permissions = new_permissions  # ChatPermissions

    @staticmethod
    def read(q: dict, *args) -> "ChatEventPermissionsChanged":
        old_permissions = Object.read(q.get('old_permissions'))
        new_permissions = Object.read(q.get('new_permissions'))
        return ChatEventPermissionsChanged(old_permissions, new_permissions)
