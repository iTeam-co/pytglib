

from ..utils import Object


class SearchMessagesFilterPinned(Object):
    """
    Returns only pinned messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterPinned``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterPinned"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterPinned":
        
        return SearchMessagesFilterPinned()
