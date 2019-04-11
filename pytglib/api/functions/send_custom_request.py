

from ..utils import Object


class SendCustomRequest(Object):
    """
    Sends a custom request; for bots only 

    Attributes:
        ID (:obj:`str`): ``SendCustomRequest``

    Args:
        method (:obj:`str`):
            The method name 
        parameters (:obj:`str`):
            JSON-serialized method parameters

    Returns:
        CustomRequestResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendCustomRequest"

    def __init__(self, method, parameters, extra=None, **kwargs):
        self.extra = extra
        self.method = method  # str
        self.parameters = parameters  # str

    @staticmethod
    def read(q: dict, *args) -> "SendCustomRequest":
        method = q.get('method')
        parameters = q.get('parameters')
        return SendCustomRequest(method, parameters)
