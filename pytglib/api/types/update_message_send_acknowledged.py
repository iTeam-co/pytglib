

from ..utils import Object


class UpdateMessageSendAcknowledged(Object):
    """
    A request to send a message has reached the Telegram server. This doesn't mean that the message will be sent successfully or even that the send message request will be processed. This update will be sent only if the option "use_quick_ack" is set to true. This update may be sent multiple times for the same message

    Attributes:
        ID (:obj:`str`): ``UpdateMessageSendAcknowledged``

    Args:
        chat_id (:obj:`int`):
            The chat identifier of the sent message 
        message_id (:obj:`int`):
            A temporary message identifier

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageSendAcknowledged"

    def __init__(self, chat_id, message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageSendAcknowledged":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return UpdateMessageSendAcknowledged(chat_id, message_id)
