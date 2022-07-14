

from ..utils import Object


class SetMessageReaction(Object):
    """
    Changes chosen reaction for a message

    Attributes:
        ID (:obj:`str`): ``SetMessageReaction``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message
        reaction (:obj:`str`):
            Text representation of the new chosen reactionCan be an empty string or the currently chosen non-big reaction to remove the reaction
        is_big (:obj:`bool`):
            Pass true if the reaction is added with a big animation

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setMessageReaction"

    def __init__(self, chat_id, message_id, reaction, is_big, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reaction = reaction  # str
        self.is_big = is_big  # bool

    @staticmethod
    def read(q: dict, *args) -> "SetMessageReaction":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reaction = q.get('reaction')
        is_big = q.get('is_big')
        return SetMessageReaction(chat_id, message_id, reaction, is_big)
