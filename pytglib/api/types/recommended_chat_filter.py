

from ..utils import Object


class RecommendedChatFilter(Object):
    """
    Describes a recommended chat filter 

    Attributes:
        ID (:obj:`str`): ``RecommendedChatFilter``

    Args:
        filter (:class:`telegram.api.types.chatFilter`):
            The chat filter 
        description (:obj:`str`):
            Chat filter description

    Returns:
        RecommendedChatFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "recommendedChatFilter"

    def __init__(self, filter, description, **kwargs):
        
        self.filter = filter  # ChatFilter
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "RecommendedChatFilter":
        filter = Object.read(q.get('filter'))
        description = q.get('description')
        return RecommendedChatFilter(filter, description)
