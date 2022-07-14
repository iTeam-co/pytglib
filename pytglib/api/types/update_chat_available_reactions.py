

from ..utils import Object


class UpdateChatAvailableReactions(Object):
    """
    The chat available reactions were changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatAvailableReactions``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        available_reactions (List of :obj:`str`):
            The new list of reactions, available in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatAvailableReactions"

    def __init__(self, chat_id, available_reactions, **kwargs):
        
        self.chat_id = chat_id  # int
        self.available_reactions = available_reactions  # list of str

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatAvailableReactions":
        chat_id = q.get('chat_id')
        available_reactions = q.get('available_reactions')
        return UpdateChatAvailableReactions(chat_id, available_reactions)
