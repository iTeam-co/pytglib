

from ..utils import Object


class SearchMessagesFilterMention(Object):
    """
    Returns only messages with mentions of the current user, or messages that are replies to their messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterMention``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterMention"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterMention":
        
        return SearchMessagesFilterMention()
