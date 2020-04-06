

from ..utils import Object


class StatisticsGraphData(Object):
    """
    A graph data 

    Attributes:
        ID (:obj:`str`): ``StatisticsGraphData``

    Args:
        json_data (:obj:`str`):
            Graph data in JSON format 
        zoom_token (:obj:`str`):
            If non-empty, a token which can be used to receive a zoomed in graph

    Returns:
        StatisticsGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticsGraphData"

    def __init__(self, json_data, zoom_token, **kwargs):
        
        self.json_data = json_data  # str
        self.zoom_token = zoom_token  # str

    @staticmethod
    def read(q: dict, *args) -> "StatisticsGraphData":
        json_data = q.get('json_data')
        zoom_token = q.get('zoom_token')
        return StatisticsGraphData(json_data, zoom_token)
