

from ..utils import Object


class DisableProxy(Object):
    """
    Disables the currently enabled proxy. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``DisableProxy``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "disableProxy"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "DisableProxy":
        
        return DisableProxy()
