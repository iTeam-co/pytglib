

from ..utils import Object


class Message(Object):
    """
    Describes a message

    Attributes:
        ID (:obj:`str`): ``Message``

    Args:
        id (:obj:`int`):
            Message identifier, unique for the chat to which the message belongs
        sender_user_id (:obj:`int`):
            Identifier of the user who sent the message; 0 if unknownCurrently, it is unknown for channel posts and for channel posts automatically forwarded to discussion group
        chat_id (:obj:`int`):
            Chat identifier
        sending_state (:class:`telegram.api.types.MessageSendingState`):
            Information about the sending state of the message; may be null
        scheduling_state (:class:`telegram.api.types.MessageSchedulingState`):
            Information about the scheduling state of the message; may be null
        is_outgoing (:obj:`bool`):
            True, if the message is outgoing
        can_be_edited (:obj:`bool`):
            True, if the message can be editedFor live location and poll messages this fields shows whether editMessageLiveLocation or stopPoll can be used with this message by the client
        can_be_forwarded (:obj:`bool`):
            True, if the message can be forwarded
        can_be_deleted_only_for_self (:obj:`bool`):
            True, if the message can be deleted only for the current user while other users will continue to see it
        can_be_deleted_for_all_users (:obj:`bool`):
            True, if the message can be deleted for all users
        is_channel_post (:obj:`bool`):
            True, if the message is a channel postAll messages to channels are channel posts, all other messages are not channel posts
        contains_unread_mention (:obj:`bool`):
            True, if the message contains an unread mention for the current user
        date (:obj:`int`):
            Point in time (Unix timestamp) when the message was sent
        edit_date (:obj:`int`):
            Point in time (Unix timestamp) when the message was last edited
        forward_info (:class:`telegram.api.types.messageForwardInfo`):
            Information about the initial message sender; may be null
        reply_to_message_id (:obj:`int`):
            If non-zero, the identifier of the message this message is replying to; can be the identifier of a deleted message
        ttl (:obj:`int`):
            For self-destructing messages, the message's TTL (Time To Live), in seconds; 0 if noneTDLib will send updateDeleteMessages or updateMessageContent once the TTL expires
        ttl_expires_in (:obj:`float`):
            Time left before the message expires, in seconds
        via_bot_user_id (:obj:`int`):
            If non-zero, the user identifier of the bot through which this message was sent
        author_signature (:obj:`str`):
            For channel posts, optional author signature
        views (:obj:`int`):
            Number of times this message was viewed
        media_album_id (:obj:`int`):
            Unique identifier of an album this message belongs toOnly photos and videos can be grouped together in albums
        restriction_reason (:obj:`str`):
            If non-empty, contains a human-readable description of the reason why access to this message must be restricted
        content (:class:`telegram.api.types.MessageContent`):
            Content of the message
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            Reply markup for the message; may be null

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "message"

    def __init__(self, id, sender_user_id, chat_id, sending_state, scheduling_state, is_outgoing, can_be_edited, can_be_forwarded, can_be_deleted_only_for_self, can_be_deleted_for_all_users, is_channel_post, contains_unread_mention, date, edit_date, forward_info, reply_to_message_id, ttl, ttl_expires_in, via_bot_user_id, author_signature, views, media_album_id, restriction_reason, content, reply_markup, **kwargs):
        
        self.id = id  # int
        self.sender_user_id = sender_user_id  # int
        self.chat_id = chat_id  # int
        self.sending_state = sending_state  # MessageSendingState
        self.scheduling_state = scheduling_state  # MessageSchedulingState
        self.is_outgoing = is_outgoing  # bool
        self.can_be_edited = can_be_edited  # bool
        self.can_be_forwarded = can_be_forwarded  # bool
        self.can_be_deleted_only_for_self = can_be_deleted_only_for_self  # bool
        self.can_be_deleted_for_all_users = can_be_deleted_for_all_users  # bool
        self.is_channel_post = is_channel_post  # bool
        self.contains_unread_mention = contains_unread_mention  # bool
        self.date = date  # int
        self.edit_date = edit_date  # int
        self.forward_info = forward_info  # MessageForwardInfo
        self.reply_to_message_id = reply_to_message_id  # int
        self.ttl = ttl  # int
        self.ttl_expires_in = ttl_expires_in  # float
        self.via_bot_user_id = via_bot_user_id  # int
        self.author_signature = author_signature  # str
        self.views = views  # int
        self.media_album_id = media_album_id  # int
        self.restriction_reason = restriction_reason  # str
        self.content = content  # MessageContent
        self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(q: dict, *args) -> "Message":
        id = q.get('id')
        sender_user_id = q.get('sender_user_id')
        chat_id = q.get('chat_id')
        sending_state = Object.read(q.get('sending_state'))
        scheduling_state = Object.read(q.get('scheduling_state'))
        is_outgoing = q.get('is_outgoing')
        can_be_edited = q.get('can_be_edited')
        can_be_forwarded = q.get('can_be_forwarded')
        can_be_deleted_only_for_self = q.get('can_be_deleted_only_for_self')
        can_be_deleted_for_all_users = q.get('can_be_deleted_for_all_users')
        is_channel_post = q.get('is_channel_post')
        contains_unread_mention = q.get('contains_unread_mention')
        date = q.get('date')
        edit_date = q.get('edit_date')
        forward_info = Object.read(q.get('forward_info'))
        reply_to_message_id = q.get('reply_to_message_id')
        ttl = q.get('ttl')
        ttl_expires_in = q.get('ttl_expires_in')
        via_bot_user_id = q.get('via_bot_user_id')
        author_signature = q.get('author_signature')
        views = q.get('views')
        media_album_id = q.get('media_album_id')
        restriction_reason = q.get('restriction_reason')
        content = Object.read(q.get('content'))
        reply_markup = Object.read(q.get('reply_markup'))
        return Message(id, sender_user_id, chat_id, sending_state, scheduling_state, is_outgoing, can_be_edited, can_be_forwarded, can_be_deleted_only_for_self, can_be_deleted_for_all_users, is_channel_post, contains_unread_mention, date, edit_date, forward_info, reply_to_message_id, ttl, ttl_expires_in, via_bot_user_id, author_signature, views, media_album_id, restriction_reason, content, reply_markup)
