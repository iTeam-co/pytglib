

from ..utils import Object


class ChatMemberStatusAdministrator(Object):
    """
    The user is a member of a chat and has some additional privileges. In basic groups, administrators can edit and delete messages sent by others, add new members, and ban unprivileged members. In supergroups and channels, there are more detailed options for administrator privileges

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusAdministrator``

    Args:
        custom_title (:obj:`str`):
            A custom title of the administrator; 0-16 characters without emojis; applicable to supergroups only
        can_be_edited (:obj:`bool`):
            True, if the current user can edit the administrator privileges for the called user
        can_change_info (:obj:`bool`):
            True, if the administrator can change the chat title, photo, and other settings
        can_post_messages (:obj:`bool`):
            True, if the administrator can create channel posts; applicable to channels only
        can_edit_messages (:obj:`bool`):
            True, if the administrator can edit messages of other users and pin messages; applicable to channels only
        can_delete_messages (:obj:`bool`):
            True, if the administrator can delete messages of other users
        can_invite_users (:obj:`bool`):
            True, if the administrator can invite new users to the chat
        can_restrict_members (:obj:`bool`):
            True, if the administrator can restrict, ban, or unban chat members
        can_pin_messages (:obj:`bool`):
            True, if the administrator can pin messages; applicable to groups only
        can_promote_members (:obj:`bool`):
            True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that were directly or indirectly promoted by them

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusAdministrator"

    def __init__(self, custom_title, can_be_edited, can_change_info, can_post_messages, can_edit_messages, can_delete_messages, can_invite_users, can_restrict_members, can_pin_messages, can_promote_members, **kwargs):
        
        self.custom_title = custom_title  # str
        self.can_be_edited = can_be_edited  # bool
        self.can_change_info = can_change_info  # bool
        self.can_post_messages = can_post_messages  # bool
        self.can_edit_messages = can_edit_messages  # bool
        self.can_delete_messages = can_delete_messages  # bool
        self.can_invite_users = can_invite_users  # bool
        self.can_restrict_members = can_restrict_members  # bool
        self.can_pin_messages = can_pin_messages  # bool
        self.can_promote_members = can_promote_members  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusAdministrator":
        custom_title = q.get('custom_title')
        can_be_edited = q.get('can_be_edited')
        can_change_info = q.get('can_change_info')
        can_post_messages = q.get('can_post_messages')
        can_edit_messages = q.get('can_edit_messages')
        can_delete_messages = q.get('can_delete_messages')
        can_invite_users = q.get('can_invite_users')
        can_restrict_members = q.get('can_restrict_members')
        can_pin_messages = q.get('can_pin_messages')
        can_promote_members = q.get('can_promote_members')
        return ChatMemberStatusAdministrator(custom_title, can_be_edited, can_change_info, can_post_messages, can_edit_messages, can_delete_messages, can_invite_users, can_restrict_members, can_pin_messages, can_promote_members)
