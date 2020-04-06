

from ..utils import Object


class ChatMemberStatusRestricted(Object):
    """
    The user is under certain restrictions in the chat. Not supported in basic groups and channels

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusRestricted``

    Args:
        is_member (:obj:`bool`):
            True, if the user is a member of the chat
        restricted_until_date (:obj:`int`):
            Point in time (Unix timestamp) when restrictions will be lifted from the user; 0 if neverIf the user is restricted for more than 366 days or for less than 30 seconds from the current time, the user is considered to be restricted forever
        permissions (:class:`telegram.api.types.chatPermissions`):
            User permissions in the chat

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusRestricted"

    def __init__(self, is_member, restricted_until_date, permissions, **kwargs):
        
        self.is_member = is_member  # bool
        self.restricted_until_date = restricted_until_date  # int
        self.permissions = permissions  # ChatPermissions

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusRestricted":
        is_member = q.get('is_member')
        restricted_until_date = q.get('restricted_until_date')
        permissions = Object.read(q.get('permissions'))
        return ChatMemberStatusRestricted(is_member, restricted_until_date, permissions)
