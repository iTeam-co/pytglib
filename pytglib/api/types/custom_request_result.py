

from ..utils import Object


class CustomRequestResult(Object):
    """
    Contains the result of a custom request 

    Attributes:
        ID (:obj:`str`): ``CustomRequestResult``

    Args:
        result (:obj:`str`):
            A JSON-serialized result

    Returns:
        CustomRequestResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "customRequestResult"

    def __init__(self, result, **kwargs):
        
        self.result = result  # str

    @staticmethod
    def read(q: dict, *args) -> "CustomRequestResult":
        result = q.get('result')
        return CustomRequestResult(result)
