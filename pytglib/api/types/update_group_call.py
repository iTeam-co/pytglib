

from ..utils import Object


class UpdateGroupCall(Object):
    """
    Information about a group call was updated 

    Attributes:
        ID (:obj:`str`): ``UpdateGroupCall``

    Args:
        group_call (:class:`telegram.api.types.groupCall`):
            New data about a group call

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateGroupCall"

    def __init__(self, group_call, **kwargs):
        
        self.group_call = group_call  # GroupCall

    @staticmethod
    def read(q: dict, *args) -> "UpdateGroupCall":
        group_call = Object.read(q.get('group_call'))
        return UpdateGroupCall(group_call)
