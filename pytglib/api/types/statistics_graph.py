

from ..utils import Object


class StatisticsGraph(Object):
    """
    Descrbes a statistics graph

    No parameters required.
    """
    ID = "statisticsGraph"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "StatisticsGraphAsync or StatisticsGraphError or StatisticsGraphData":
        if q.get("@type"):
            return Object.read(q)
        return StatisticsGraph()
