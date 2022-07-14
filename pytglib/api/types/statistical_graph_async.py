

from ..utils import Object


class StatisticalGraphAsync(Object):
    """
    The graph data to be asynchronously loaded through getStatisticalGraph 

    Attributes:
        ID (:obj:`str`): ``StatisticalGraphAsync``

    Args:
        token (:obj:`str`):
            The token to use for data loading

    Returns:
        StatisticalGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticalGraphAsync"

    def __init__(self, token, **kwargs):
        
        self.token = token  # str

    @staticmethod
    def read(q: dict, *args) -> "StatisticalGraphAsync":
        token = q.get('token')
        return StatisticalGraphAsync(token)
