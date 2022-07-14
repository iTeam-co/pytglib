

from ..utils import Object


class UpdateMessageUnreadReactions(Object):
    """
    The list of unread reactions added to a message was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageUnreadReactions``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        unread_reactions (List of :class:`telegram.api.types.unreadReaction`):
            The new list of unread reactions 
        unread_reaction_count (:obj:`int`):
            The new number of messages with unread reactions left in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageUnreadReactions"

    def __init__(self, chat_id, message_id, unread_reactions, unread_reaction_count, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.unread_reactions = unread_reactions  # list of unreadReaction
        self.unread_reaction_count = unread_reaction_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageUnreadReactions":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        unread_reactions = [Object.read(i) for i in q.get('unread_reactions', [])]
        unread_reaction_count = q.get('unread_reaction_count')
        return UpdateMessageUnreadReactions(chat_id, message_id, unread_reactions, unread_reaction_count)
