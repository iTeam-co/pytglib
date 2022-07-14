

from ..utils import Object


class TargetChatCurrent(Object):
    """
    The currently opened chat needs to be kept

    Attributes:
        ID (:obj:`str`): ``TargetChatCurrent``

    No parameters required.

    Returns:
        TargetChat

    Raises:
        :class:`telegram.Error`
    """
    ID = "targetChatCurrent"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TargetChatCurrent":
        
        return TargetChatCurrent()
