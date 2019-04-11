

from ..utils import Object


class TopChatCategoryChannels(Object):
    """
    A category containing frequently used channels

    Attributes:
        ID (:obj:`str`): ``TopChatCategoryChannels``

    No parameters required.

    Returns:
        TopChatCategory

    Raises:
        :class:`telegram.Error`
    """
    ID = "topChatCategoryChannels"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryChannels":
        
        return TopChatCategoryChannels()
