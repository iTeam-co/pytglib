

from ..utils import Object


class Seconds(Object):
    """
    Contains a value representing a number of seconds 

    Attributes:
        ID (:obj:`str`): ``Seconds``

    Args:
        seconds (:obj:`float`):
            Number of seconds

    Returns:
        Seconds

    Raises:
        :class:`telegram.Error`
    """
    ID = "seconds"

    def __init__(self, seconds, **kwargs):
        
        self.seconds = seconds  # float

    @staticmethod
    def read(q: dict, *args) -> "Seconds":
        seconds = q.get('seconds')
        return Seconds(seconds)
