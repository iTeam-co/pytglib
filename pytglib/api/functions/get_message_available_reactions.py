

from ..utils import Object


class GetMessageAvailableReactions(Object):
    """
    Returns reactions, which can be added to a message. The list can change after updateReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message. The method will return Premium reactions, even the current user has no Premium subscription

    Attributes:
        ID (:obj:`str`): ``GetMessageAvailableReactions``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message

    Returns:
        AvailableReactions

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageAvailableReactions"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageAvailableReactions":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetMessageAvailableReactions(chat_id, message_id)
