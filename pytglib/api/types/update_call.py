

from ..utils import Object


class UpdateCall(Object):
    """
    New call was created or information about a call was updated 

    Attributes:
        ID (:obj:`str`): ``UpdateCall``

    Args:
        call (:class:`telegram.api.types.call`):
            New data about a call

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateCall"

    def __init__(self, call, **kwargs):
        
        self.call = call  # Call

    @staticmethod
    def read(q: dict, *args) -> "UpdateCall":
        call = Object.read(q.get('call'))
        return UpdateCall(call)
