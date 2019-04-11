

from ..utils import Object


class TopChatCategoryBots(Object):
    """
    A category containing frequently used private chats with bot users

    Attributes:
        ID (:obj:`str`): ``TopChatCategoryBots``

    No parameters required.

    Returns:
        TopChatCategory

    Raises:
        :class:`telegram.Error`
    """
    ID = "topChatCategoryBots"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryBots":
        
        return TopChatCategoryBots()
