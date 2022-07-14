

from ..utils import Object


class Message(Object):
    """
    Describes a message

    Attributes:
        ID (:obj:`str`): ``Message``

    Args:
        id (:obj:`int`):
            Message identifier; unique for the chat to which the message belongs
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the sender of the message
        chat_id (:obj:`int`):
            Chat identifier
        sending_state (:class:`telegram.api.types.MessageSendingState`):
            The sending state of the message; may be null
        scheduling_state (:class:`telegram.api.types.MessageSchedulingState`):
            The scheduling state of the message; may be null
        is_outgoing (:obj:`bool`):
            True, if the message is outgoing
        is_pinned (:obj:`bool`):
            True, if the message is pinned
        can_be_edited (:obj:`bool`):
            True, if the message can be editedFor live location and poll messages this fields shows whether editMessageLiveLocation or stopPoll can be used with this message by the application
        can_be_forwarded (:obj:`bool`):
            True, if the message can be forwarded
        can_be_saved (:obj:`bool`):
            True, if content of the message can be saved locally or copied
        can_be_deleted_only_for_self (:obj:`bool`):
            True, if the message can be deleted only for the current user while other users will continue to see it
        can_be_deleted_for_all_users (:obj:`bool`):
            True, if the message can be deleted for all users
        can_get_added_reactions (:obj:`bool`):
            True, if the list of added reactions is available through getMessageAddedReactions
        can_get_statistics (:obj:`bool`):
            True, if the message statistics are available through getMessageStatistics
        can_get_message_thread (:obj:`bool`):
            True, if information about the message thread is available through getMessageThread
        can_get_viewers (:obj:`bool`):
            True, if chat members already viewed the message can be received through getMessageViewers
        can_get_media_timestamp_links (:obj:`bool`):
            True, if media timestamp links can be generated for media timestamp entities in the message text, caption or web page description through getMessageLink
        has_timestamped_media (:obj:`bool`):
            True, if media timestamp entities refers to a media in this message as opposed to a media in the replied message
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
        interaction_info (:class:`telegram.api.types.messageInteractionInfo`):
            Information about interactions with the message; may be null
        unread_reactions (List of :class:`telegram.api.types.unreadReaction`):
            Information about unread reactions added to the message
        reply_in_chat_id (:obj:`int`):
            If non-zero, the identifier of the chat to which the replied message belongs; Currently, only messages in the Replies chat can have different reply_in_chat_id and chat_id
        reply_to_message_id (:obj:`int`):
            If non-zero, the identifier of the message this message is replying to; can be the identifier of a deleted message
        message_thread_id (:obj:`int`):
            If non-zero, the identifier of the message thread the message belongs to; unique within the chat to which the message belongs
        ttl (:obj:`int`):
            For self-destructing messages, the message's TTL (Time To Live), in seconds; 0 if noneTDLib will send updateDeleteMessages or updateMessageContent once the TTL expires
        ttl_expires_in (:obj:`float`):
            Time left before the message expires, in secondsIf the TTL timer isn't started yet, equals to the value of the ttl field
        via_bot_user_id (:obj:`int`):
            If non-zero, the user identifier of the bot through which this message was sent
        author_signature (:obj:`str`):
            For channel posts and anonymous group messages, optional author signature
        media_album_id (:obj:`int`):
            Unique identifier of an album this message belongs toOnly audios, documents, photos and videos can be grouped together in albums
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

    def __init__(self, id, sender_id, chat_id, sending_state, scheduling_state, is_outgoing, is_pinned, can_be_edited, can_be_forwarded, can_be_saved, can_be_deleted_only_for_self, can_be_deleted_for_all_users, can_get_added_reactions, can_get_statistics, can_get_message_thread, can_get_viewers, can_get_media_timestamp_links, has_timestamped_media, is_channel_post, contains_unread_mention, date, edit_date, forward_info, interaction_info, unread_reactions, reply_in_chat_id, reply_to_message_id, message_thread_id, ttl, ttl_expires_in, via_bot_user_id, author_signature, media_album_id, restriction_reason, content, reply_markup, **kwargs):
        
        self.id = id  # int
        self.sender_id = sender_id  # MessageSender
        self.chat_id = chat_id  # int
        self.sending_state = sending_state  # MessageSendingState
        self.scheduling_state = scheduling_state  # MessageSchedulingState
        self.is_outgoing = is_outgoing  # bool
        self.is_pinned = is_pinned  # bool
        self.can_be_edited = can_be_edited  # bool
        self.can_be_forwarded = can_be_forwarded  # bool
        self.can_be_saved = can_be_saved  # bool
        self.can_be_deleted_only_for_self = can_be_deleted_only_for_self  # bool
        self.can_be_deleted_for_all_users = can_be_deleted_for_all_users  # bool
        self.can_get_added_reactions = can_get_added_reactions  # bool
        self.can_get_statistics = can_get_statistics  # bool
        self.can_get_message_thread = can_get_message_thread  # bool
        self.can_get_viewers = can_get_viewers  # bool
        self.can_get_media_timestamp_links = can_get_media_timestamp_links  # bool
        self.has_timestamped_media = has_timestamped_media  # bool
        self.is_channel_post = is_channel_post  # bool
        self.contains_unread_mention = contains_unread_mention  # bool
        self.date = date  # int
        self.edit_date = edit_date  # int
        self.forward_info = forward_info  # MessageForwardInfo
        self.interaction_info = interaction_info  # MessageInteractionInfo
        self.unread_reactions = unread_reactions  # list of unreadReaction
        self.reply_in_chat_id = reply_in_chat_id  # int
        self.reply_to_message_id = reply_to_message_id  # int
        self.message_thread_id = message_thread_id  # int
        self.ttl = ttl  # int
        self.ttl_expires_in = ttl_expires_in  # float
        self.via_bot_user_id = via_bot_user_id  # int
        self.author_signature = author_signature  # str
        self.media_album_id = media_album_id  # int
        self.restriction_reason = restriction_reason  # str
        self.content = content  # MessageContent
        self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(q: dict, *args) -> "Message":
        id = q.get('id')
        sender_id = Object.read(q.get('sender_id'))
        chat_id = q.get('chat_id')
        sending_state = Object.read(q.get('sending_state'))
        scheduling_state = Object.read(q.get('scheduling_state'))
        is_outgoing = q.get('is_outgoing')
        is_pinned = q.get('is_pinned')
        can_be_edited = q.get('can_be_edited')
        can_be_forwarded = q.get('can_be_forwarded')
        can_be_saved = q.get('can_be_saved')
        can_be_deleted_only_for_self = q.get('can_be_deleted_only_for_self')
        can_be_deleted_for_all_users = q.get('can_be_deleted_for_all_users')
        can_get_added_reactions = q.get('can_get_added_reactions')
        can_get_statistics = q.get('can_get_statistics')
        can_get_message_thread = q.get('can_get_message_thread')
        can_get_viewers = q.get('can_get_viewers')
        can_get_media_timestamp_links = q.get('can_get_media_timestamp_links')
        has_timestamped_media = q.get('has_timestamped_media')
        is_channel_post = q.get('is_channel_post')
        contains_unread_mention = q.get('contains_unread_mention')
        date = q.get('date')
        edit_date = q.get('edit_date')
        forward_info = Object.read(q.get('forward_info'))
        interaction_info = Object.read(q.get('interaction_info'))
        unread_reactions = [Object.read(i) for i in q.get('unread_reactions', [])]
        reply_in_chat_id = q.get('reply_in_chat_id')
        reply_to_message_id = q.get('reply_to_message_id')
        message_thread_id = q.get('message_thread_id')
        ttl = q.get('ttl')
        ttl_expires_in = q.get('ttl_expires_in')
        via_bot_user_id = q.get('via_bot_user_id')
        author_signature = q.get('author_signature')
        media_album_id = q.get('media_album_id')
        restriction_reason = q.get('restriction_reason')
        content = Object.read(q.get('content'))
        reply_markup = Object.read(q.get('reply_markup'))
        return Message(id, sender_id, chat_id, sending_state, scheduling_state, is_outgoing, is_pinned, can_be_edited, can_be_forwarded, can_be_saved, can_be_deleted_only_for_self, can_be_deleted_for_all_users, can_get_added_reactions, can_get_statistics, can_get_message_thread, can_get_viewers, can_get_media_timestamp_links, has_timestamped_media, is_channel_post, contains_unread_mention, date, edit_date, forward_info, interaction_info, unread_reactions, reply_in_chat_id, reply_to_message_id, message_thread_id, ttl, ttl_expires_in, via_bot_user_id, author_signature, media_album_id, restriction_reason, content, reply_markup)
