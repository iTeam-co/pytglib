

from ..utils import Object


class Chat(Object):
    """
    A chat. (Can be a private chat, basic group, supergroup, or secret chat)

    Attributes:
        ID (:obj:`str`): ``Chat``

    Args:
        id (:obj:`int`):
            Chat unique identifier
        type (:class:`telegram.api.types.ChatType`):
            Type of the chat
        chat_list (:class:`telegram.api.types.ChatList`):
            A chat list to which the chat belongs; may be null
        title (:obj:`str`):
            Chat title
        photo (:class:`telegram.api.types.chatPhoto`):
            Chat photo; may be null
        permissions (:class:`telegram.api.types.chatPermissions`):
            Actions that non-administrator chat members are allowed to take in the chat
        last_message (:class:`telegram.api.types.message`):
            Last message in the chat; may be null
        order (:obj:`int`):
            Descending parameter by which chats are sorted in the main chat listIf the order number of two chats is the same, they must be sorted in descending order by IDIf 0, the position of the chat in the list is undetermined
        is_pinned (:obj:`bool`):
            True, if the chat is pinned
        is_marked_as_unread (:obj:`bool`):
            True, if the chat is marked as unread
        is_sponsored (:obj:`bool`):
            True, if the chat is sponsored by the user's MTProxy server
        has_scheduled_messages (:obj:`bool`):
            True, if the chat has scheduled messages
        can_be_deleted_only_for_self (:obj:`bool`):
            True, if the chat messages can be deleted only for the current user while other users will continue to see the messages
        can_be_deleted_for_all_users (:obj:`bool`):
            True, if the chat messages can be deleted for all users
        can_be_reported (:obj:`bool`):
            True, if the chat can be reported to Telegram moderators through reportChat
        default_disable_notification (:obj:`bool`):
            Default value of the disable_notification parameter, used when a message is sent to the chat
        unread_count (:obj:`int`):
            Number of unread messages in the chat
        last_read_inbox_message_id (:obj:`int`):
            Identifier of the last read incoming message
        last_read_outbox_message_id (:obj:`int`):
            Identifier of the last read outgoing message
        unread_mention_count (:obj:`int`):
            Number of unread messages with a mention/reply in the chat
        notification_settings (:class:`telegram.api.types.chatNotificationSettings`):
            Notification settings for this chat
        action_bar (:class:`telegram.api.types.ChatActionBar`):
            Describes actions which should be possible to do through a chat action bar; may be null
        pinned_message_id (:obj:`int`):
            Identifier of the pinned message in the chat; 0 if none
        reply_markup_message_id (:obj:`int`):
            Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
        draft_message (:class:`telegram.api.types.draftMessage`):
            A draft of a message in the chat; may be null
        client_data (:obj:`str`):
            Contains client-specific data associated with the chat(For example, the chat position or local chat notification settings can be stored here) Persistent if the message database is used

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "chat"

    def __init__(self, id, type, chat_list, title, photo, permissions, last_message, order, is_pinned, is_marked_as_unread, is_sponsored, has_scheduled_messages, can_be_deleted_only_for_self, can_be_deleted_for_all_users, can_be_reported, default_disable_notification, unread_count, last_read_inbox_message_id, last_read_outbox_message_id, unread_mention_count, notification_settings, action_bar, pinned_message_id, reply_markup_message_id, draft_message, client_data, **kwargs):
        
        self.id = id  # int
        self.type = type  # ChatType
        self.chat_list = chat_list  # ChatList
        self.title = title  # str
        self.photo = photo  # ChatPhoto
        self.permissions = permissions  # ChatPermissions
        self.last_message = last_message  # Message
        self.order = order  # int
        self.is_pinned = is_pinned  # bool
        self.is_marked_as_unread = is_marked_as_unread  # bool
        self.is_sponsored = is_sponsored  # bool
        self.has_scheduled_messages = has_scheduled_messages  # bool
        self.can_be_deleted_only_for_self = can_be_deleted_only_for_self  # bool
        self.can_be_deleted_for_all_users = can_be_deleted_for_all_users  # bool
        self.can_be_reported = can_be_reported  # bool
        self.default_disable_notification = default_disable_notification  # bool
        self.unread_count = unread_count  # int
        self.last_read_inbox_message_id = last_read_inbox_message_id  # int
        self.last_read_outbox_message_id = last_read_outbox_message_id  # int
        self.unread_mention_count = unread_mention_count  # int
        self.notification_settings = notification_settings  # ChatNotificationSettings
        self.action_bar = action_bar  # ChatActionBar
        self.pinned_message_id = pinned_message_id  # int
        self.reply_markup_message_id = reply_markup_message_id  # int
        self.draft_message = draft_message  # DraftMessage
        self.client_data = client_data  # str

    @staticmethod
    def read(q: dict, *args) -> "Chat":
        id = q.get('id')
        type = Object.read(q.get('type'))
        chat_list = Object.read(q.get('chat_list'))
        title = q.get('title')
        photo = Object.read(q.get('photo'))
        permissions = Object.read(q.get('permissions'))
        last_message = Object.read(q.get('last_message'))
        order = q.get('order')
        is_pinned = q.get('is_pinned')
        is_marked_as_unread = q.get('is_marked_as_unread')
        is_sponsored = q.get('is_sponsored')
        has_scheduled_messages = q.get('has_scheduled_messages')
        can_be_deleted_only_for_self = q.get('can_be_deleted_only_for_self')
        can_be_deleted_for_all_users = q.get('can_be_deleted_for_all_users')
        can_be_reported = q.get('can_be_reported')
        default_disable_notification = q.get('default_disable_notification')
        unread_count = q.get('unread_count')
        last_read_inbox_message_id = q.get('last_read_inbox_message_id')
        last_read_outbox_message_id = q.get('last_read_outbox_message_id')
        unread_mention_count = q.get('unread_mention_count')
        notification_settings = Object.read(q.get('notification_settings'))
        action_bar = Object.read(q.get('action_bar'))
        pinned_message_id = q.get('pinned_message_id')
        reply_markup_message_id = q.get('reply_markup_message_id')
        draft_message = Object.read(q.get('draft_message'))
        client_data = q.get('client_data')
        return Chat(id, type, chat_list, title, photo, permissions, last_message, order, is_pinned, is_marked_as_unread, is_sponsored, has_scheduled_messages, can_be_deleted_only_for_self, can_be_deleted_for_all_users, can_be_reported, default_disable_notification, unread_count, last_read_inbox_message_id, last_read_outbox_message_id, unread_mention_count, notification_settings, action_bar, pinned_message_id, reply_markup_message_id, draft_message, client_data)
