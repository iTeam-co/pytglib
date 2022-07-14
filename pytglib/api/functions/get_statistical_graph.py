

from ..utils import Object


class GetStatisticalGraph(Object):
    """
    Loads an asynchronous or a zoomed in statistical graph 

    Attributes:
        ID (:obj:`str`): ``GetStatisticalGraph``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        token (:obj:`str`):
            The token for graph loading 
        x (:obj:`int`):
            X-value for zoomed in graph or 0 otherwise

    Returns:
        StatisticalGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "getStatisticalGraph"

    def __init__(self, chat_id, token, x, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.token = token  # str
        self.x = x  # int

    @staticmethod
    def read(q: dict, *args) -> "GetStatisticalGraph":
        chat_id = q.get('chat_id')
        token = q.get('token')
        x = q.get('x')
        return GetStatisticalGraph(chat_id, token, x)
