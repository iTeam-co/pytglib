

from ..utils import Object


class AvailableReactions(Object):
    """
    Represents a list of available reactions 

    Attributes:
        ID (:obj:`str`): ``AvailableReactions``

    Args:
        reactions (List of :class:`telegram.api.types.availableReaction`):
            List of reactions

    Returns:
        AvailableReactions

    Raises:
        :class:`telegram.Error`
    """
    ID = "availableReactions"

    def __init__(self, reactions, **kwargs):
        
        self.reactions = reactions  # list of availableReaction

    @staticmethod
    def read(q: dict, *args) -> "AvailableReactions":
        reactions = [Object.read(i) for i in q.get('reactions', [])]
        return AvailableReactions(reactions)
