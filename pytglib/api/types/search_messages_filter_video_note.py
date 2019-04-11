

from ..utils import Object


class SearchMessagesFilterVideoNote(Object):
    """
    Returns only video note messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterVideoNote``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterVideoNote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterVideoNote":
        
        return SearchMessagesFilterVideoNote()
