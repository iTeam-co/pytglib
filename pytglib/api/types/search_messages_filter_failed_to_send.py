

from ..utils import Object


class SearchMessagesFilterFailedToSend(Object):
    """
    Returns only failed to send messages. This filter can be used only if the message database is used

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterFailedToSend``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterFailedToSend"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterFailedToSend":
        
        return SearchMessagesFilterFailedToSend()
