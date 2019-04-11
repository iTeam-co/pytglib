

from ..utils import Object


class SetAlarm(Object):
    """
    Succeeds after a specified amount of time has passed. Can be called before authorization. Can be called before initialization 

    Attributes:
        ID (:obj:`str`): ``SetAlarm``

    Args:
        seconds (:obj:`float`):
            Number of seconds before the function returns

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setAlarm"

    def __init__(self, seconds, extra=None, **kwargs):
        self.extra = extra
        self.seconds = seconds  # float

    @staticmethod
    def read(q: dict, *args) -> "SetAlarm":
        seconds = q.get('seconds')
        return SetAlarm(seconds)
