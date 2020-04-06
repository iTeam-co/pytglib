

from ..utils import Object


class ResendMessages(Object):
    """
    Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed.If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message

    Attributes:
        ID (:obj:`str`): ``ResendMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to send messages 
        message_ids (List of :obj:`int`):
            Identifiers of the messages to resendMessage identifiers must be in a strictly increasing order

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "resendMessages"

    def __init__(self, chat_id, message_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_ids = message_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ResendMessages":
        chat_id = q.get('chat_id')
        message_ids = q.get('message_ids')
        return ResendMessages(chat_id, message_ids)
