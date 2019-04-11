

from ..utils import Object


class SearchMessagesFilterAudio(Object):
    """
    Returns only audio messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterAudio``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterAudio"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterAudio":
        
        return SearchMessagesFilterAudio()
