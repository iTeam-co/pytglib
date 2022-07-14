

from ..utils import Object


class CancelPasswordReset(Object):
    """
    Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0

    Attributes:
        ID (:obj:`str`): ``CancelPasswordReset``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "cancelPasswordReset"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "CancelPasswordReset":
        
        return CancelPasswordReset()
