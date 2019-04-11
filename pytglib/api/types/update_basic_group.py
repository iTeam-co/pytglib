

from ..utils import Object


class UpdateBasicGroup(Object):
    """
    Some data of a basic group has changed. This update is guaranteed to come before the basic group identifier is returned to the client 

    Attributes:
        ID (:obj:`str`): ``UpdateBasicGroup``

    Args:
        basic_group (:class:`telegram.api.types.basicGroup`):
            New data about the group

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateBasicGroup"

    def __init__(self, basic_group, **kwargs):
        
        self.basic_group = basic_group  # BasicGroup

    @staticmethod
    def read(q: dict, *args) -> "UpdateBasicGroup":
        basic_group = Object.read(q.get('basic_group'))
        return UpdateBasicGroup(basic_group)
