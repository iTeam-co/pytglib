

from ..utils import Object


class DeleteSavedOrderInfo(Object):
    """
    Deletes saved order info

    Attributes:
        ID (:obj:`str`): ``DeleteSavedOrderInfo``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteSavedOrderInfo"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "DeleteSavedOrderInfo":
        
        return DeleteSavedOrderInfo()
