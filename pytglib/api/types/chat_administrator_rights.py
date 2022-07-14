

from ..utils import Object


class ChatAdministratorRights(Object):
    """
    Describes rights of the administrator

    Attributes:
        ID (:obj:`str`): ``ChatAdministratorRights``

    Args:
        can_manage_chat (:obj:`bool`):
            True, if the administrator can get chat event log, get chat statistics, get message statistics in channels, get channel members, see anonymous administrators in supergroups and ignore slow modeImplied by any other privilege; applicable to supergroups and channels only
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
            True, if the administrator can restrict, ban, or unban chat members; always true for channels
        can_pin_messages (:obj:`bool`):
            True, if the administrator can pin messages; applicable to basic groups and supergroups only
        can_promote_members (:obj:`bool`):
            True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that were directly or indirectly promoted by them
        can_manage_video_chats (:obj:`bool`):
            True, if the administrator can manage video chats
        is_anonymous (:obj:`bool`):
            True, if the administrator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only

    Returns:
        ChatAdministratorRights

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatAdministratorRights"

    def __init__(self, can_manage_chat, can_change_info, can_post_messages, can_edit_messages, can_delete_messages, can_invite_users, can_restrict_members, can_pin_messages, can_promote_members, can_manage_video_chats, is_anonymous, **kwargs):
        
        self.can_manage_chat = can_manage_chat  # bool
        self.can_change_info = can_change_info  # bool
        self.can_post_messages = can_post_messages  # bool
        self.can_edit_messages = can_edit_messages  # bool
        self.can_delete_messages = can_delete_messages  # bool
        self.can_invite_users = can_invite_users  # bool
        self.can_restrict_members = can_restrict_members  # bool
        self.can_pin_messages = can_pin_messages  # bool
        self.can_promote_members = can_promote_members  # bool
        self.can_manage_video_chats = can_manage_video_chats  # bool
        self.is_anonymous = is_anonymous  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatAdministratorRights":
        can_manage_chat = q.get('can_manage_chat')
        can_change_info = q.get('can_change_info')
        can_post_messages = q.get('can_post_messages')
        can_edit_messages = q.get('can_edit_messages')
        can_delete_messages = q.get('can_delete_messages')
        can_invite_users = q.get('can_invite_users')
        can_restrict_members = q.get('can_restrict_members')
        can_pin_messages = q.get('can_pin_messages')
        can_promote_members = q.get('can_promote_members')
        can_manage_video_chats = q.get('can_manage_video_chats')
        is_anonymous = q.get('is_anonymous')
        return ChatAdministratorRights(can_manage_chat, can_change_info, can_post_messages, can_edit_messages, can_delete_messages, can_invite_users, can_restrict_members, can_pin_messages, can_promote_members, can_manage_video_chats, is_anonymous)
