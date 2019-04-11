

from ..utils import Object


class SearchMessagesFilterVoiceAndVideoNote(Object):
    """
    Returns only voice and video note messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterVoiceAndVideoNote``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterVoiceAndVideoNote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterVoiceAndVideoNote":
        
        return SearchMessagesFilterVoiceAndVideoNote()
