

from ..utils import Object


class UpdateChatReadInbox(Object):
    """
    Incoming messages were read or number of unread messages has been changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatReadInbox``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        last_read_inbox_message_id (:obj:`int`):
            Identifier of the last read incoming message 
        unread_count (:obj:`int`):
            The number of unread messages left in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatReadInbox"

    def __init__(self, chat_id, last_read_inbox_message_id, unread_count, **kwargs):
        
        self.chat_id = chat_id  # int
        self.last_read_inbox_message_id = last_read_inbox_message_id  # int
        self.unread_count = unread_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatReadInbox":
        chat_id = q.get('chat_id')
        last_read_inbox_message_id = q.get('last_read_inbox_message_id')
        unread_count = q.get('unread_count')
        return UpdateChatReadInbox(chat_id, last_read_inbox_message_id, unread_count)
