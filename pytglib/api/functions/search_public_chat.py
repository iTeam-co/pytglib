

from ..utils import Object


class SearchPublicChat(Object):
    """
    Searches a public chat by its username. Currently only private chats, supergroups and channels can be public. Returns the chat if found; otherwise an error is returned 

    Attributes:
        ID (:obj:`str`): ``SearchPublicChat``

    Args:
        username (:obj:`str`):
            Username to be resolved

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchPublicChat"

    def __init__(self, username, extra=None, **kwargs):
        self.extra = extra
        self.username = username  # str

    @staticmethod
    def read(q: dict, *args) -> "SearchPublicChat":
        username = q.get('username')
        return SearchPublicChat(username)
