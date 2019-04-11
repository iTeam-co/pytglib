

from ..utils import Object


class AcceptCall(Object):
    """
    Accepts an incoming call 

    Attributes:
        ID (:obj:`str`): ``AcceptCall``

    Args:
        call_id (:obj:`int`):
            Call identifier 
        protocol (:class:`telegram.api.types.callProtocol`):
            Description of the call protocols supported by the client

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "acceptCall"

    def __init__(self, call_id, protocol, extra=None, **kwargs):
        self.extra = extra
        self.call_id = call_id  # int
        self.protocol = protocol  # CallProtocol

    @staticmethod
    def read(q: dict, *args) -> "AcceptCall":
        call_id = q.get('call_id')
        protocol = Object.read(q.get('protocol'))
        return AcceptCall(call_id, protocol)
