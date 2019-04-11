

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
        title (:obj:`str`):
            Chat title
        photo (:class:`telegram.api.types.chatPhoto`):
            Chat photo; may be null
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
        reply_markup_message_id (:obj:`int`):
            Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
        draft_message (:class:`telegram.api.types.draftMessage`):
            A draft of a message in the chat; may be null
        client_data (:obj:`str`):
            Contains client-specific data associated with the chat(For example, the chat position or local chat notification settings can be stored here) Persistent if a message database is used

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "chat"

    def __init__(self, id, type, title, photo, last_message, order, is_pinned, is_marked_as_unread, is_sponsored, can_be_reported, default_disable_notification, unread_count, last_read_inbox_message_id, last_read_outbox_message_id, unread_mention_count, notification_settings, reply_markup_message_id, draft_message, client_data, **kwargs):
        
        self.id = id  # int
        self.type = type  # ChatType
        self.title = title  # str
        self.photo = photo  # ChatPhoto
        self.last_message = last_message  # Message
        self.order = order  # int
        self.is_pinned = is_pinned  # bool
        self.is_marked_as_unread = is_marked_as_unread  # bool
        self.is_sponsored = is_sponsored  # bool
        self.can_be_reported = can_be_reported  # bool
        self.default_disable_notification = default_disable_notification  # bool
        self.unread_count = unread_count  # int
        self.last_read_inbox_message_id = last_read_inbox_message_id  # int
        self.last_read_outbox_message_id = last_read_outbox_message_id  # int
        self.unread_mention_count = unread_mention_count  # int
        self.notification_settings = notification_settings  # ChatNotificationSettings
        self.reply_markup_message_id = reply_markup_message_id  # int
        self.draft_message = draft_message  # DraftMessage
        self.client_data = client_data  # str

    @staticmethod
    def read(q: dict, *args) -> "Chat":
        id = q.get('id')
        type = Object.read(q.get('type'))
        title = q.get('title')
        photo = Object.read(q.get('photo'))
        last_message = Object.read(q.get('last_message'))
        order = q.get('order')
        is_pinned = q.get('is_pinned')
        is_marked_as_unread = q.get('is_marked_as_unread')
        is_sponsored = q.get('is_sponsored')
        can_be_reported = q.get('can_be_reported')
        default_disable_notification = q.get('default_disable_notification')
        unread_count = q.get('unread_count')
        last_read_inbox_message_id = q.get('last_read_inbox_message_id')
        last_read_outbox_message_id = q.get('last_read_outbox_message_id')
        unread_mention_count = q.get('unread_mention_count')
        notification_settings = Object.read(q.get('notification_settings'))
        reply_markup_message_id = q.get('reply_markup_message_id')
        draft_message = Object.read(q.get('draft_message'))
        client_data = q.get('client_data')
        return Chat(id, type, title, photo, last_message, order, is_pinned, is_marked_as_unread, is_sponsored, can_be_reported, default_disable_notification, unread_count, last_read_inbox_message_id, last_read_outbox_message_id, unread_mention_count, notification_settings, reply_markup_message_id, draft_message, client_data)
