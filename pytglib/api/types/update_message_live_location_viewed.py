

from ..utils import Object


class UpdateMessageLiveLocationViewed(Object):
    """
    A message with a live location was viewed. When the update is received, the client is supposed to update the live location

    Attributes:
        ID (:obj:`str`): ``UpdateMessageLiveLocationViewed``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat with the live location message 
        message_id (:obj:`int`):
            Identifier of the message with live location

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageLiveLocationViewed"

    def __init__(self, chat_id, message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageLiveLocationViewed":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return UpdateMessageLiveLocationViewed(chat_id, message_id)
