

from ..utils import Object


class StatisticsGraphError(Object):
    """
    An error message to be shown to the user instead of the graph 

    Attributes:
        ID (:obj:`str`): ``StatisticsGraphError``

    Args:
        error_message (:obj:`str`):
            The error message

    Returns:
        StatisticsGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticsGraphError"

    def __init__(self, error_message, **kwargs):
        
        self.error_message = error_message  # str

    @staticmethod
    def read(q: dict, *args) -> "StatisticsGraphError":
        error_message = q.get('error_message')
        return StatisticsGraphError(error_message)
