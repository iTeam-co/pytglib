

from ..utils import Object


class UnreadReaction(Object):
    """
    Contains information about an unread reaction to a message

    Attributes:
        ID (:obj:`str`): ``UnreadReaction``

    Args:
        reaction (:obj:`str`):
            Text representation of the reaction
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the sender, added the reaction
        is_big (:obj:`bool`):
            True, if the reaction was added with a big animation

    Returns:
        UnreadReaction

    Raises:
        :class:`telegram.Error`
    """
    ID = "unreadReaction"

    def __init__(self, reaction, sender_id, is_big, **kwargs):
        
        self.reaction = reaction  # str
        self.sender_id = sender_id  # MessageSender
        self.is_big = is_big  # bool

    @staticmethod
    def read(q: dict, *args) -> "UnreadReaction":
        reaction = q.get('reaction')
        sender_id = Object.read(q.get('sender_id'))
        is_big = q.get('is_big')
        return UnreadReaction(reaction, sender_id, is_big)
