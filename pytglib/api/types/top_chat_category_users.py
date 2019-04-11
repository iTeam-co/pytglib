

from ..utils import Object


class TopChatCategoryUsers(Object):
    """
    A category containing frequently used private chats with non-bot users

    Attributes:
        ID (:obj:`str`): ``TopChatCategoryUsers``

    No parameters required.

    Returns:
        TopChatCategory

    Raises:
        :class:`telegram.Error`
    """
    ID = "topChatCategoryUsers"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryUsers":
        
        return TopChatCategoryUsers()
