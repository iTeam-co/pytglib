

from ..utils import Object


class TopChatCategoryForwardChats(Object):
    """
    A category containing frequently used chats used to forward messages

    Attributes:
        ID (:obj:`str`): ``TopChatCategoryForwardChats``

    No parameters required.

    Returns:
        TopChatCategory

    Raises:
        :class:`telegram.Error`
    """
    ID = "topChatCategoryForwardChats"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryForwardChats":
        
        return TopChatCategoryForwardChats()
