

from ..utils import Object


class StatisticalGraphError(Object):
    """
    An error message to be shown to the user instead of the graph 

    Attributes:
        ID (:obj:`str`): ``StatisticalGraphError``

    Args:
        error_message (:obj:`str`):
            The error message

    Returns:
        StatisticalGraph

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticalGraphError"

    def __init__(self, error_message, **kwargs):
        
        self.error_message = error_message  # str

    @staticmethod
    def read(q: dict, *args) -> "StatisticalGraphError":
        error_message = q.get('error_message')
        return StatisticalGraphError(error_message)
