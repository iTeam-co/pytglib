

from ..utils import Object


class StatisticalGraph(Object):
    """
    Describes a statistical graph

    No parameters required.
    """
    ID = "statisticalGraph"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "StatisticalGraphError or StatisticalGraphData or StatisticalGraphAsync":
        if q.get("@type"):
            return Object.read(q)
        return StatisticalGraph()
