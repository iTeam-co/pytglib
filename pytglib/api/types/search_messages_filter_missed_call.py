

from ..utils import Object


class SearchMessagesFilterMissedCall(Object):
    """
    Returns only incoming call messages with missed/declined discard reasons

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterMissedCall``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterMissedCall"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterMissedCall":
        
        return SearchMessagesFilterMissedCall()
