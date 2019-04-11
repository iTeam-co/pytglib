

from ..utils import Object


class SearchMessagesFilterUrl(Object):
    """
    Returns only messages containing URLs

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterUrl``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterUrl"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterUrl":
        
        return SearchMessagesFilterUrl()
