

from ..utils import Object


class TopChatCategoryGroups(Object):
    """
    A category containing frequently used basic groups and supergroups

    Attributes:
        ID (:obj:`str`): ``TopChatCategoryGroups``

    No parameters required.

    Returns:
        TopChatCategory

    Raises:
        :class:`telegram.Error`
    """
    ID = "topChatCategoryGroups"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryGroups":
        
        return TopChatCategoryGroups()
