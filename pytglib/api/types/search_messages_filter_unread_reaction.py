

from ..utils import Object


class SearchMessagesFilterUnreadReaction(Object):
    """
    Returns only messages with unread reactions for the current user. When using this filter the results can't be additionally filtered by a query, a message thread or by the sending user

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterUnreadReaction``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterUnreadReaction"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterUnreadReaction":
        
        return SearchMessagesFilterUnreadReaction()
