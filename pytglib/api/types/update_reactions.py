

from ..utils import Object


class UpdateReactions(Object):
    """
    The list of supported reactions has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateReactions``

    Args:
        reactions (List of :class:`telegram.api.types.reaction`):
            The new list of supported reactions

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateReactions"

    def __init__(self, reactions, **kwargs):
        
        self.reactions = reactions  # list of reaction

    @staticmethod
    def read(q: dict, *args) -> "UpdateReactions":
        reactions = [Object.read(i) for i in q.get('reactions', [])]
        return UpdateReactions(reactions)
