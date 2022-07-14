

from ..utils import Object


class GetMessageAddedReactions(Object):
    """
    Returns reactions added for a message, along with their sender

    Attributes:
        ID (:obj:`str`): ``GetMessageAddedReactions``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message
        reaction (:obj:`str`):
            If non-empty, only added reactions with the specified text representation will be returned
        offset (:obj:`str`):
            Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        limit (:obj:`int`):
            The maximum number of reactions to be returned; must be positive and can't be greater than 100

    Returns:
        AddedReactions

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageAddedReactions"

    def __init__(self, chat_id, message_id, reaction, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reaction = reaction  # str
        self.offset = offset  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageAddedReactions":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reaction = q.get('reaction')
        offset = q.get('offset')
        limit = q.get('limit')
        return GetMessageAddedReactions(chat_id, message_id, reaction, offset, limit)
