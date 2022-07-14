

from ..utils import Object


class MessageReplyInfo(Object):
    """
    Contains information about replies to a message

    Attributes:
        ID (:obj:`str`): ``MessageReplyInfo``

    Args:
        reply_count (:obj:`int`):
            Number of times the message was directly or indirectly replied
        recent_replier_ids (List of :class:`telegram.api.types.MessageSender`):
            Identifiers of at most 3 recent repliers to the message; available in channels with a discussion supergroupThe users and chats are expected to be inaccessible: only their photo and name will be available
        last_read_inbox_message_id (:obj:`int`):
            Identifier of the last read incoming reply to the message
        last_read_outbox_message_id (:obj:`int`):
            Identifier of the last read outgoing reply to the message
        last_message_id (:obj:`int`):
            Identifier of the last reply to the message

    Returns:
        MessageReplyInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageReplyInfo"

    def __init__(self, reply_count, recent_replier_ids, last_read_inbox_message_id, last_read_outbox_message_id, last_message_id, **kwargs):
        
        self.reply_count = reply_count  # int
        self.recent_replier_ids = recent_replier_ids  # list of MessageSender
        self.last_read_inbox_message_id = last_read_inbox_message_id  # int
        self.last_read_outbox_message_id = last_read_outbox_message_id  # int
        self.last_message_id = last_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageReplyInfo":
        reply_count = q.get('reply_count')
        recent_replier_ids = [Object.read(i) for i in q.get('recent_replier_ids', [])]
        last_read_inbox_message_id = q.get('last_read_inbox_message_id')
        last_read_outbox_message_id = q.get('last_read_outbox_message_id')
        last_message_id = q.get('last_message_id')
        return MessageReplyInfo(reply_count, recent_replier_ids, last_read_inbox_message_id, last_read_outbox_message_id, last_message_id)
