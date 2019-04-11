

from ..utils import Object


class UpdateChatUnreadMentionCount(Object):
    """
    The chat unread_mention_count has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatUnreadMentionCount``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        unread_mention_count (:obj:`int`):
            The number of unread mention messages left in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatUnreadMentionCount"

    def __init__(self, chat_id, unread_mention_count, **kwargs):
        
        self.chat_id = chat_id  # int
        self.unread_mention_count = unread_mention_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatUnreadMentionCount":
        chat_id = q.get('chat_id')
        unread_mention_count = q.get('unread_mention_count')
        return UpdateChatUnreadMentionCount(chat_id, unread_mention_count)
