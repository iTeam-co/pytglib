

from ..utils import Object


class UpdateChatReadOutbox(Object):
    """
    Outgoing messages were read 

    Attributes:
        ID (:obj:`str`): ``UpdateChatReadOutbox``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        last_read_outbox_message_id (:obj:`int`):
            Identifier of last read outgoing message

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatReadOutbox"

    def __init__(self, chat_id, last_read_outbox_message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.last_read_outbox_message_id = last_read_outbox_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatReadOutbox":
        chat_id = q.get('chat_id')
        last_read_outbox_message_id = q.get('last_read_outbox_message_id')
        return UpdateChatReadOutbox(chat_id, last_read_outbox_message_id)
