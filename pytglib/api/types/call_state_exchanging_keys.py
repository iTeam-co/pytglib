

from ..utils import Object


class CallStateExchangingKeys(Object):
    """
    The call has been answered and encryption keys are being exchanged

    Attributes:
        ID (:obj:`str`): ``CallStateExchangingKeys``

    No parameters required.

    Returns:
        CallState

    Raises:
        :class:`telegram.Error`
    """
    ID = "callStateExchangingKeys"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallStateExchangingKeys":
        
        return CallStateExchangingKeys()
