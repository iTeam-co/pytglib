

from ..utils import Object


class Count(Object):
    """
    Contains a counter 

    Attributes:
        ID (:obj:`str`): ``Count``

    Args:
        count (:obj:`int`):
            Count

    Returns:
        Count

    Raises:
        :class:`telegram.Error`
    """
    ID = "count"

    def __init__(self, count, **kwargs):
        
        self.count = count  # int

    @staticmethod
    def read(q: dict, *args) -> "Count":
        count = q.get('count')
        return Count(count)
