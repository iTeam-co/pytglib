

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
        photo (:class:`telegram.api.types.chatPhotoInfo`):
            Chat photo; may be null
        permissions (:class:`telegram.api.types.chatPermissions`):
            Actions that non-administrator chat members are allowed to take in the chat
        last_message (:class:`telegram.api.types.message`):
            Last message in the chat; may be null
        positions (List of :class:`telegram.api.types.chatPosition`):
            Positions of the chat in chat lists
        message_sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of a user or chat that is selected to send messages in the chat; may be null if the user can't change message sender
        has_protected_content (:obj:`bool`):
            True, if chat content can't be saved locally, forwarded, or copied
        is_marked_as_unread (:obj:`bool`):
            True, if the chat is marked as unread
        is_blocked (:obj:`bool`):
            True, if the chat is blocked by the current user and private messages from the chat can't be received
        has_scheduled_messages (:obj:`bool`):
            True, if the chat has scheduled messages
        can_be_deleted_only_for_self (:obj:`bool`):
            True, if the chat messages can be deleted only for the current user while other users will continue to see the messages
        can_be_deleted_for_all_users (:obj:`bool`):
            True, if the chat messages can be deleted for all users
        can_be_reported (:obj:`bool`):
            True, if the chat can be reported to Telegram moderators through reportChat or reportChatPhoto
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
        unread_reaction_count (:obj:`int`):
            Number of messages with unread reactions in the chat
        notification_settings (:class:`telegram.api.types.chatNotificationSettings`):
            Notification settings for the chat
        available_reactions (List of :obj:`str`):
            List of reactions, available in the chat
        message_ttl (:obj:`int`):
            Current message Time To Live setting (self-destruct timer) for the chat; 0 if not definedTTL is counted from the time message or its content is viewed in secret chats and from the send date in other chats
        theme_name (:obj:`str`):
            If non-empty, name of a theme, set for the chat
        action_bar (:class:`telegram.api.types.ChatActionBar`):
            Information about actions which must be possible to do through the chat action bar; may be null
        video_chat (:class:`telegram.api.types.videoChat`):
            Information about video chat of the chat
        pending_join_requests (:class:`telegram.api.types.chatJoinRequestsInfo`):
            Information about pending join requests; may be null
        reply_markup_message_id (:obj:`int`):
            Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
        draft_message (:class:`telegram.api.types.draftMessage`):
            A draft of a message in the chat; may be null
        client_data (:obj:`str`):
            Application-specific data associated with the chat(For example, the chat scroll position or local chat notification settings can be stored here) Persistent if the message database is used

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "chat"

    def __init__(self, id, type, title, photo, permissions, last_message, positions, message_sender_id, has_protected_content, is_marked_as_unread, is_blocked, has_scheduled_messages, can_be_deleted_only_for_self, can_be_deleted_for_all_users, can_be_reported, default_disable_notification, unread_count, last_read_inbox_message_id, last_read_outbox_message_id, unread_mention_count, unread_reaction_count, notification_settings, available_reactions, message_ttl, theme_name, action_bar, video_chat, pending_join_requests, reply_markup_message_id, draft_message, client_data, **kwargs):
        
        self.id = id  # int
        self.type = type  # ChatType
        self.title = title  # str
        self.photo = photo  # ChatPhotoInfo
        self.permissions = permissions  # ChatPermissions
        self.last_message = last_message  # Message
        self.positions = positions  # list of chatPosition
        self.message_sender_id = message_sender_id  # MessageSender
        self.has_protected_content = has_protected_content  # bool
        self.is_marked_as_unread = is_marked_as_unread  # bool
        self.is_blocked = is_blocked  # bool
        self.has_scheduled_messages = has_scheduled_messages  # bool
        self.can_be_deleted_only_for_self = can_be_deleted_only_for_self  # bool
        self.can_be_deleted_for_all_users = can_be_deleted_for_all_users  # bool
        self.can_be_reported = can_be_reported  # bool
        self.default_disable_notification = default_disable_notification  # bool
        self.unread_count = unread_count  # int
        self.last_read_inbox_message_id = last_read_inbox_message_id  # int
        self.last_read_outbox_message_id = last_read_outbox_message_id  # int
        self.unread_mention_count = unread_mention_count  # int
        self.unread_reaction_count = unread_reaction_count  # int
        self.notification_settings = notification_settings  # ChatNotificationSettings
        self.available_reactions = available_reactions  # list of str
        self.message_ttl = message_ttl  # int
        self.theme_name = theme_name  # str
        self.action_bar = action_bar  # ChatActionBar
        self.video_chat = video_chat  # VideoChat
        self.pending_join_requests = pending_join_requests  # ChatJoinRequestsInfo
        self.reply_markup_message_id = reply_markup_message_id  # int
        self.draft_message = draft_message  # DraftMessage
        self.client_data = client_data  # str

    @staticmethod
    def read(q: dict, *args) -> "Chat":
        id = q.get('id')
        type = Object.read(q.get('type'))
        title = q.get('title')
        photo = Object.read(q.get('photo'))
        permissions = Object.read(q.get('permissions'))
        last_message = Object.read(q.get('last_message'))
        positions = [Object.read(i) for i in q.get('positions', [])]
        message_sender_id = Object.read(q.get('message_sender_id'))
        has_protected_content = q.get('has_protected_content')
        is_marked_as_unread = q.get('is_marked_as_unread')
        is_blocked = q.get('is_blocked')
        has_scheduled_messages = q.get('has_scheduled_messages')
        can_be_deleted_only_for_self = q.get('can_be_deleted_only_for_self')
        can_be_deleted_for_all_users = q.get('can_be_deleted_for_all_users')
        can_be_reported = q.get('can_be_reported')
        default_disable_notification = q.get('default_disable_notification')
        unread_count = q.get('unread_count')
        last_read_inbox_message_id = q.get('last_read_inbox_message_id')
        last_read_outbox_message_id = q.get('last_read_outbox_message_id')
        unread_mention_count = q.get('unread_mention_count')
        unread_reaction_count = q.get('unread_reaction_count')
        notification_settings = Object.read(q.get('notification_settings'))
        available_reactions = q.get('available_reactions')
        message_ttl = q.get('message_ttl')
        theme_name = q.get('theme_name')
        action_bar = Object.read(q.get('action_bar'))
        video_chat = Object.read(q.get('video_chat'))
        pending_join_requests = Object.read(q.get('pending_join_requests'))
        reply_markup_message_id = q.get('reply_markup_message_id')
        draft_message = Object.read(q.get('draft_message'))
        client_data = q.get('client_data')
        return Chat(id, type, title, photo, permissions, last_message, positions, message_sender_id, has_protected_content, is_marked_as_unread, is_blocked, has_scheduled_messages, can_be_deleted_only_for_self, can_be_deleted_for_all_users, can_be_reported, default_disable_notification, unread_count, last_read_inbox_message_id, last_read_outbox_message_id, unread_mention_count, unread_reaction_count, notification_settings, available_reactions, message_ttl, theme_name, action_bar, video_chat, pending_join_requests, reply_markup_message_id, draft_message, client_data)
