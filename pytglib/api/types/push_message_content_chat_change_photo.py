

from ..utils import Object


class PushMessageContentChatChangePhoto(Object):
    """
    A chat photo was edited

    Attributes:
        ID (:obj:`str`): ``PushMessageContentChatChangePhoto``

    No parameters required.

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentChatChangePhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatChangePhoto":
        
        return PushMessageContentChatChangePhoto()
