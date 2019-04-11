

from ..utils import Object


class MessageSupergroupChatCreate(Object):
    """
    A newly created supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``MessageSupergroupChatCreate``

    Args:
        title (:obj:`str`):
            Title of the supergroup or channel

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSupergroupChatCreate"

    def __init__(self, title, **kwargs):
        
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageSupergroupChatCreate":
        title = q.get('title')
        return MessageSupergroupChatCreate(title)
