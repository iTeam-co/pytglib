

from ..utils import Object


class ChatMemberStatusAdministrator(Object):
    """
    The user is a member of the chat and has some additional privileges. In basic groups, administrators can edit and delete messages sent by others, add new members, ban unprivileged members, and manage video chats. In supergroups and channels, there are more detailed options for administrator privileges

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusAdministrator``

    Args:
        custom_title (:obj:`str`):
            A custom title of the administrator; 0-16 characters without emojis; applicable to supergroups only
        can_be_edited (:obj:`bool`):
            True, if the current user can edit the administrator privileges for the called user
        rights (:class:`telegram.api.types.chatAdministratorRights`):
            Rights of the administrator

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusAdministrator"

    def __init__(self, custom_title, can_be_edited, rights, **kwargs):
        
        self.custom_title = custom_title  # str
        self.can_be_edited = can_be_edited  # bool
        self.rights = rights  # ChatAdministratorRights

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusAdministrator":
        custom_title = q.get('custom_title')
        can_be_edited = q.get('can_be_edited')
        rights = Object.read(q.get('rights'))
        return ChatMemberStatusAdministrator(custom_title, can_be_edited, rights)
