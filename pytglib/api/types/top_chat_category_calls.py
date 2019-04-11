

from ..utils import Object


class TopChatCategoryCalls(Object):
    """
    A category containing frequently used chats used for calls

    Attributes:
        ID (:obj:`str`): ``TopChatCategoryCalls``

    No parameters required.

    Returns:
        TopChatCategory

    Raises:
        :class:`telegram.Error`
    """
    ID = "topChatCategoryCalls"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryCalls":
        
        return TopChatCategoryCalls()
