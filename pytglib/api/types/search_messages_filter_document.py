

from ..utils import Object


class SearchMessagesFilterDocument(Object):
    """
    Returns only document messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterDocument``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterDocument"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterDocument":
        
        return SearchMessagesFilterDocument()
