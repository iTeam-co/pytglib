

from ..utils import Object


class AvailableReaction(Object):
    """
    Represents an available reaction 

    Attributes:
        ID (:obj:`str`): ``AvailableReaction``

    Args:
        reaction (:obj:`str`):
            Text representation of the reaction 
        needs_premium (:obj:`bool`):
            True, if Telegram Premium is needed to send the reaction

    Returns:
        AvailableReaction

    Raises:
        :class:`telegram.Error`
    """
    ID = "availableReaction"

    def __init__(self, reaction, needs_premium, **kwargs):
        
        self.reaction = reaction  # str
        self.needs_premium = needs_premium  # bool

    @staticmethod
    def read(q: dict, *args) -> "AvailableReaction":
        reaction = q.get('reaction')
        needs_premium = q.get('needs_premium')
        return AvailableReaction(reaction, needs_premium)
