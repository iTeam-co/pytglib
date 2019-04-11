

from ..utils import Object


class SetTdlibParameters(Object):
    """
    Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters 

    Attributes:
        ID (:obj:`str`): ``SetTdlibParameters``

    Args:
        parameters (:class:`telegram.api.types.tdlibParameters`):
            Parameters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setTdlibParameters"

    def __init__(self, parameters, extra=None, **kwargs):
        self.extra = extra
        self.parameters = parameters  # TdlibParameters

    @staticmethod
    def read(q: dict, *args) -> "SetTdlibParameters":
        parameters = Object.read(q.get('parameters'))
        return SetTdlibParameters(parameters)
