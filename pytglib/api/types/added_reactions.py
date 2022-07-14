

from ..utils import Object


class AddedReactions(Object):
    """
    Represents a list of reactions added to a message 

    Attributes:
        ID (:obj:`str`): ``AddedReactions``

    Args:
        total_count (:obj:`int`):
            The total number of found reactions 
        reactions (List of :class:`telegram.api.types.addedReaction`):
            The list of added reactions 
        next_offset (:obj:`str`):
            The offset for the next requestIf empty, there are no more results

    Returns:
        AddedReactions

    Raises:
        :class:`telegram.Error`
    """
    ID = "addedReactions"

    def __init__(self, total_count, reactions, next_offset, **kwargs):
        
        self.total_count = total_count  # int
        self.reactions = reactions  # list of addedReaction
        self.next_offset = next_offset  # str

    @staticmethod
    def read(q: dict, *args) -> "AddedReactions":
        total_count = q.get('total_count')
        reactions = [Object.read(i) for i in q.get('reactions', [])]
        next_offset = q.get('next_offset')
        return AddedReactions(total_count, reactions, next_offset)
