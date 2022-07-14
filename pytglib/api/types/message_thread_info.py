

from ..utils import Object


class MessageThreadInfo(Object):
    """
    Contains information about a message thread

    Attributes:
        ID (:obj:`str`): ``MessageThreadInfo``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message thread belongs
        message_thread_id (:obj:`int`):
            Message thread identifier, unique within the chat
        reply_info (:class:`telegram.api.types.messageReplyInfo`):
            Information about the message thread
        unread_message_count (:obj:`int`):
            Approximate number of unread messages in the message thread
        messages (List of :class:`telegram.api.types.message`):
            The messages from which the thread startsThe messages are returned in a reverse chronological order (ie, in order of decreasing message_id)
        draft_message (:class:`telegram.api.types.draftMessage`):
            A draft of a message in the message thread; may be null

    Returns:
        MessageThreadInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageThreadInfo"

    def __init__(self, chat_id, message_thread_id, reply_info, unread_message_count, messages, draft_message, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_thread_id = message_thread_id  # int
        self.reply_info = reply_info  # MessageReplyInfo
        self.unread_message_count = unread_message_count  # int
        self.messages = messages  # list of message
        self.draft_message = draft_message  # DraftMessage

    @staticmethod
    def read(q: dict, *args) -> "MessageThreadInfo":
        chat_id = q.get('chat_id')
        message_thread_id = q.get('message_thread_id')
        reply_info = Object.read(q.get('reply_info'))
        unread_message_count = q.get('unread_message_count')
        messages = [Object.read(i) for i in q.get('messages', [])]
        draft_message = Object.read(q.get('draft_message'))
        return MessageThreadInfo(chat_id, message_thread_id, reply_info, unread_message_count, messages, draft_message)
