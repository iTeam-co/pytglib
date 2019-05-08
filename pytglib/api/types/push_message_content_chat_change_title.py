

from ..utils import Object


class PushMessageContentChatChangeTitle(Object):
    """
    A chat title was edited 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentChatChangeTitle``

    Args:
        title (:obj:`str`):
            New chat title

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentChatChangeTitle"

    def __init__(self, title, **kwargs):
        
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatChangeTitle":
        title = q.get('title')
        return PushMessageContentChatChangeTitle(title)
