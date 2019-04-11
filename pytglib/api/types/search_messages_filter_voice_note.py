

from ..utils import Object


class SearchMessagesFilterVoiceNote(Object):
    """
    Returns only voice note messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterVoiceNote``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterVoiceNote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterVoiceNote":
        
        return SearchMessagesFilterVoiceNote()
