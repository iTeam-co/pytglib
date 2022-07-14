

from ..utils import Object


class StatisticalGraphData(Object):
    """
    A graph data 

    Attributes:
        ID (:obj:`str`): ``StatisticalGraphData``

    Args:
        json_data (:obj:`str`):
            Graph data in JSON format 
        zoom_token (:obj:`str`):
            If non-empty, a token which can be used to receive a zoomed in graph

    Returns:
        StatisticalGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticalGraphData"

    def __init__(self, json_data, zoom_token, **kwargs):
        
        self.json_data = json_data  # str
        self.zoom_token = zoom_token  # str

    @staticmethod
    def read(q: dict, *args) -> "StatisticalGraphData":
        json_data = q.get('json_data')
        zoom_token = q.get('zoom_token')
        return StatisticalGraphData(json_data, zoom_token)
