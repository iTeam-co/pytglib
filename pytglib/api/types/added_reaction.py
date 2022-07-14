

from ..utils import Object


class AddedReaction(Object):
    """
    Represents a reaction applied to a message 

    Attributes:
        ID (:obj:`str`): ``AddedReaction``

    Args:
        reaction (:obj:`str`):
            Text representation of the reaction 
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the chat member, applied the reaction

    Returns:
        AddedReaction

    Raises:
        :class:`telegram.Error`
    """
    ID = "addedReaction"

    def __init__(self, reaction, sender_id, **kwargs):
        
        self.reaction = reaction  # str
        self.sender_id = sender_id  # MessageSender

    @staticmethod
    def read(q: dict, *args) -> "AddedReaction":
        reaction = q.get('reaction')
        sender_id = Object.read(q.get('sender_id'))
        return AddedReaction(reaction, sender_id)
