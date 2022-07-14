

from ..utils import Object


class SetChatAvailableReactions(Object):
    """
    Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right 

    Attributes:
        ID (:obj:`str`): ``SetChatAvailableReactions``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat 
        available_reactions (List of :obj:`str`):
            New list of reactions, available in the chatAll reactions must be active

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatAvailableReactions"

    def __init__(self, chat_id, available_reactions, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.available_reactions = available_reactions  # list of str

    @staticmethod
    def read(q: dict, *args) -> "SetChatAvailableReactions":
        chat_id = q.get('chat_id')
        available_reactions = q.get('available_reactions')
        return SetChatAvailableReactions(chat_id, available_reactions)
