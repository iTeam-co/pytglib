

from ..utils import Object


class PushMessageContentBasicGroupChatCreate(Object):
    """
    A newly created basic group

    Attributes:
        ID (:obj:`str`): ``PushMessageContentBasicGroupChatCreate``

    No parameters required.

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentBasicGroupChatCreate"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentBasicGroupChatCreate":
        
        return PushMessageContentBasicGroupChatCreate()
