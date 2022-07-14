

from ..utils import Object


class UpdateChatUnreadReactionCount(Object):
    """
    The chat unread_reaction_count has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatUnreadReactionCount``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        unread_reaction_count (:obj:`int`):
            The number of messages with unread reactions left in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatUnreadReactionCount"

    def __init__(self, chat_id, unread_reaction_count, **kwargs):
        
        self.chat_id = chat_id  # int
        self.unread_reaction_count = unread_reaction_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatUnreadReactionCount":
        chat_id = q.get('chat_id')
        unread_reaction_count = q.get('unread_reaction_count')
        return UpdateChatUnreadReactionCount(chat_id, unread_reaction_count)
