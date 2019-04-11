

from ..utils import Object


class TopChatCategoryInlineBots(Object):
    """
    A category containing frequently used chats with inline bots sorted by their usage in inline mode

    Attributes:
        ID (:obj:`str`): ``TopChatCategoryInlineBots``

    No parameters required.

    Returns:
        TopChatCategory

    Raises:
        :class:`telegram.Error`
    """
    ID = "topChatCategoryInlineBots"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryInlineBots":
        
        return TopChatCategoryInlineBots()
