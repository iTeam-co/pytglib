

from ..utils import Object


class ChatEventAvailableReactionsChanged(Object):
    """
    The chat available reactions were changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventAvailableReactionsChanged``

    Args:
        old_available_reactions (List of :obj:`str`):
            Previous chat available reactions 
        new_available_reactions (List of :obj:`str`):
            New chat available reactions

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventAvailableReactionsChanged"

    def __init__(self, old_available_reactions, new_available_reactions, **kwargs):
        
        self.old_available_reactions = old_available_reactions  # list of str
        self.new_available_reactions = new_available_reactions  # list of str

    @staticmethod
    def read(q: dict, *args) -> "ChatEventAvailableReactionsChanged":
        old_available_reactions = q.get('old_available_reactions')
        new_available_reactions = q.get('new_available_reactions')
        return ChatEventAvailableReactionsChanged(old_available_reactions, new_available_reactions)
