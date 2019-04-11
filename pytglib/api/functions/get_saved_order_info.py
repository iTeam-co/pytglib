

from ..utils import Object


class GetSavedOrderInfo(Object):
    """
    Returns saved order info, if any

    Attributes:
        ID (:obj:`str`): ``GetSavedOrderInfo``

    No parameters required.

    Returns:
        OrderInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSavedOrderInfo"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetSavedOrderInfo":
        
        return GetSavedOrderInfo()
