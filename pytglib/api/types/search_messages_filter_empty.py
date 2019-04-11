

from ..utils import Object


class SearchMessagesFilterEmpty(Object):
    """
    Returns all found messages, no filter is applied

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterEmpty``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterEmpty"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterEmpty":
        
        return SearchMessagesFilterEmpty()
