

from ..utils import Object


class CreateCall(Object):
    """
    Creates a new call 

    Attributes:
        ID (:obj:`str`): ``CreateCall``

    Args:
        user_id (:obj:`int`):
            Identifier of the user to be called 
        protocol (:class:`telegram.api.types.callProtocol`):
            Description of the call protocols supported by the client

    Returns:
        CallId

    Raises:
        :class:`telegram.Error`
    """
    ID = "createCall"

    def __init__(self, user_id, protocol, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.protocol = protocol  # CallProtocol

    @staticmethod
    def read(q: dict, *args) -> "CreateCall":
        user_id = q.get('user_id')
        protocol = Object.read(q.get('protocol'))
        return CreateCall(user_id, protocol)
