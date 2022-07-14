

from ..utils import Object


class GetRecommendedChatFilters(Object):
    """
    Returns recommended chat filters for the current user

    Attributes:
        ID (:obj:`str`): ``GetRecommendedChatFilters``

    No parameters required.

    Returns:
        RecommendedChatFilters

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRecommendedChatFilters"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetRecommendedChatFilters":
        
        return GetRecommendedChatFilters()
