

from ..utils import Object


class GetChat(Object):
    """
    Returns information about a chat by its identifier, this is an offline request if the current user is not a bot 

    Attributes:
        ID (:obj:`str`): ``GetChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChat":
        chat_id = q.get('chat_id')
        return GetChat(chat_id)
