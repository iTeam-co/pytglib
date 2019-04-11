

from ..utils import Object


class ChatEventTitleChanged(Object):
    """
    The chat title was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventTitleChanged``

    Args:
        old_title (:obj:`str`):
            Previous chat title 
        new_title (:obj:`str`):
            New chat title

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventTitleChanged"

    def __init__(self, old_title, new_title, **kwargs):
        
        self.old_title = old_title  # str
        self.new_title = new_title  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatEventTitleChanged":
        old_title = q.get('old_title')
        new_title = q.get('new_title')
        return ChatEventTitleChanged(old_title, new_title)
