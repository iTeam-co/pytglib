

from ..utils import Object


class MessageReaction(Object):
    """
    Contains information about a reaction to a message

    Attributes:
        ID (:obj:`str`): ``MessageReaction``

    Args:
        reaction (:obj:`str`):
            Text representation of the reaction
        total_count (:obj:`int`):
            Number of times the reaction was added
        is_chosen (:obj:`bool`):
            True, if the reaction is chosen by the current user
        recent_sender_ids (List of :class:`telegram.api.types.MessageSender`):
            Identifiers of at most 3 recent message senders, added the reaction; available in private, basic group and supergroup chats

    Returns:
        MessageReaction

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageReaction"

    def __init__(self, reaction, total_count, is_chosen, recent_sender_ids, **kwargs):
        
        self.reaction = reaction  # str
        self.total_count = total_count  # int
        self.is_chosen = is_chosen  # bool
        self.recent_sender_ids = recent_sender_ids  # list of MessageSender

    @staticmethod
    def read(q: dict, *args) -> "MessageReaction":
        reaction = q.get('reaction')
        total_count = q.get('total_count')
        is_chosen = q.get('is_chosen')
        recent_sender_ids = [Object.read(i) for i in q.get('recent_sender_ids', [])]
        return MessageReaction(reaction, total_count, is_chosen, recent_sender_ids)
