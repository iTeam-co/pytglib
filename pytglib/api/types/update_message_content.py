

from ..utils import Object


class UpdateMessageContent(Object):
    """
    The message content has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageContent``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        new_content (:class:`telegram.api.types.MessageContent`):
            New message content

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageContent"

    def __init__(self, chat_id, message_id, new_content, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.new_content = new_content  # MessageContent

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageContent":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        new_content = Object.read(q.get('new_content'))
        return UpdateMessageContent(chat_id, message_id, new_content)
