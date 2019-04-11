

from ..utils import Object


class SearchMessagesFilterCall(Object):
    """
    Returns only call messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterCall``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterCall"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterCall":
        
        return SearchMessagesFilterCall()
