

from ..utils import Object


class UpdateSupergroupFullInfo(Object):
    """
    Some data from supergroupFullInfo has been changed 

    Attributes:
        ID (:obj:`str`): ``UpdateSupergroupFullInfo``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel 
        supergroup_full_info (:class:`telegram.api.types.supergroupFullInfo`):
            New full information about the supergroup

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateSupergroupFullInfo"

    def __init__(self, supergroup_id, supergroup_full_info, **kwargs):
        
        self.supergroup_id = supergroup_id  # int
        self.supergroup_full_info = supergroup_full_info  # SupergroupFullInfo

    @staticmethod
    def read(q: dict, *args) -> "UpdateSupergroupFullInfo":
        supergroup_id = q.get('supergroup_id')
        supergroup_full_info = Object.read(q.get('supergroup_full_info'))
        return UpdateSupergroupFullInfo(supergroup_id, supergroup_full_info)
