

from ..utils import Object


class SearchMessagesFilterVideo(Object):
    """
    Returns only video messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterVideo``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterVideo":
        
        return SearchMessagesFilterVideo()
