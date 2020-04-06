

from ..utils import Object


class StatisticsGraphAsync(Object):
    """
    The graph data to be asynchronously loaded through getChatStatisticsGraph 

    Attributes:
        ID (:obj:`str`): ``StatisticsGraphAsync``

    Args:
        token (:obj:`str`):
            The token to use for data loading

    Returns:
        StatisticsGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticsGraphAsync"

    def __init__(self, token, **kwargs):
        
        self.token = token  # str

    @staticmethod
    def read(q: dict, *args) -> "StatisticsGraphAsync":
        token = q.get('token')
        return StatisticsGraphAsync(token)
