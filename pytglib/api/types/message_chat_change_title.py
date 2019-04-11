

from ..utils import Object


class MessageChatChangeTitle(Object):
    """
    An updated chat title 

    Attributes:
        ID (:obj:`str`): ``MessageChatChangeTitle``

    Args:
        title (:obj:`str`):
            New chat title

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatChangeTitle"

    def __init__(self, title, **kwargs):
        
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageChatChangeTitle":
        title = q.get('title')
        return MessageChatChangeTitle(title)
