

from ..utils import Object


class GetChatStatisticsGraph(Object):
    """
    Loads asynchronous or zoomed in chat statistics graph 

    Attributes:
        ID (:obj:`str`): ``GetChatStatisticsGraph``

    Args:
        chat_id (:obj:`int`):
            Chat identifer 
        token (:obj:`str`):
            The token for graph loading 
        x (:obj:`int`):
            X-value for zoomed in graph or 0 otherwise

    Returns:
        StatisticsGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatStatisticsGraph"

    def __init__(self, chat_id, token, x, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.token = token  # str
        self.x = x  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatStatisticsGraph":
        chat_id = q.get('chat_id')
        token = q.get('token')
        x = q.get('x')
        return GetChatStatisticsGraph(chat_id, token, x)
