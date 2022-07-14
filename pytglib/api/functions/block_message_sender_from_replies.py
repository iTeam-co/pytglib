

from ..utils import Object


class BlockMessageSenderFromReplies(Object):
    """
    Blocks an original sender of a message in the Replies chat

    Attributes:
        ID (:obj:`str`): ``BlockMessageSenderFromReplies``

    Args:
        message_id (:obj:`int`):
            The identifier of an incoming message in the Replies chat
        delete_message (:obj:`bool`):
            Pass true to delete the message
        delete_all_messages (:obj:`bool`):
            Pass true to delete all messages from the same sender
        report_spam (:obj:`bool`):
            Pass true to report the sender to the Telegram moderators

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "blockMessageSenderFromReplies"

    def __init__(self, message_id, delete_message, delete_all_messages, report_spam, extra=None, **kwargs):
        self.extra = extra
        self.message_id = message_id  # int
        self.delete_message = delete_message  # bool
        self.delete_all_messages = delete_all_messages  # bool
        self.report_spam = report_spam  # bool

    @staticmethod
    def read(q: dict, *args) -> "BlockMessageSenderFromReplies":
        message_id = q.get('message_id')
        delete_message = q.get('delete_message')
        delete_all_messages = q.get('delete_all_messages')
        report_spam = q.get('report_spam')
        return BlockMessageSenderFromReplies(message_id, delete_message, delete_all_messages, report_spam)
