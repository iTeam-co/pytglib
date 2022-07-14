

from ..utils import Object


class RecommendedChatFilters(Object):
    """
    Contains a list of recommended chat filters 

    Attributes:
        ID (:obj:`str`): ``RecommendedChatFilters``

    Args:
        chat_filters (List of :class:`telegram.api.types.recommendedChatFilter`):
            List of recommended chat filters

    Returns:
        RecommendedChatFilters

    Raises:
        :class:`telegram.Error`
    """
    ID = "recommendedChatFilters"

    def __init__(self, chat_filters, **kwargs):
        
        self.chat_filters = chat_filters  # list of recommendedChatFilter

    @staticmethod
    def read(q: dict, *args) -> "RecommendedChatFilters":
        chat_filters = [Object.read(i) for i in q.get('chat_filters', [])]
        return RecommendedChatFilters(chat_filters)
