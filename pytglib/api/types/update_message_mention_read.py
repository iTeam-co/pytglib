

from ..utils import Object


class UpdateMessageMentionRead(Object):
    """
    A message with an unread mention was read 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageMentionRead``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        unread_mention_count (:obj:`int`):
            The new number of unread mention messages left in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageMentionRead"

    def __init__(self, chat_id, message_id, unread_mention_count, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.unread_mention_count = unread_mention_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageMentionRead":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        unread_mention_count = q.get('unread_mention_count')
        return UpdateMessageMentionRead(chat_id, message_id, unread_mention_count)
