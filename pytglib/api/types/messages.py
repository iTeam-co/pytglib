

from ..utils import Object


class Messages(Object):
    """
    Contains a list of messages 

    Attributes:
        ID (:obj:`str`): ``Messages``

    Args:
        total_count (:obj:`int`):
            Approximate total count of messages found 
        messages (List of :class:`telegram.api.types.message`):
            List of messages; messages may be null

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "messages"

    def __init__(self, total_count, messages, **kwargs):
        
        self.total_count = total_count  # int
        self.messages = messages  # list of message

    @staticmethod
    def read(q: dict, *args) -> "Messages":
        total_count = q.get('total_count')
        messages = [Object.read(i) for i in q.get('messages', [])]
        return Messages(total_count, messages)
