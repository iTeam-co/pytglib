

from ..utils import Object


class SearchMessagesFilterChatPhoto(Object):
    """
    Returns only messages containing chat photos

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterChatPhoto``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterChatPhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterChatPhoto":
        
        return SearchMessagesFilterChatPhoto()
