

from ..utils import Object


class SearchMessagesFilterUnreadMention(Object):
    """
    Returns only messages with unread mentions of the current user, or messages that are replies to their messages. When using this filter the results can't be additionally filtered by a query or by the sending user

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterUnreadMention``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterUnreadMention"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterUnreadMention":
        
        return SearchMessagesFilterUnreadMention()
