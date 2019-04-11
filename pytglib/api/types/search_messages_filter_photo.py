

from ..utils import Object


class SearchMessagesFilterPhoto(Object):
    """
    Returns only photo messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterPhoto``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterPhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterPhoto":
        
        return SearchMessagesFilterPhoto()
