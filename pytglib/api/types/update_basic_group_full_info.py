

from ..utils import Object


class UpdateBasicGroupFullInfo(Object):
    """
    Some data from basicGroupFullInfo has been changed 

    Attributes:
        ID (:obj:`str`): ``UpdateBasicGroupFullInfo``

    Args:
        basic_group_id (:obj:`int`):
            Identifier of a basic group 
        basic_group_full_info (:class:`telegram.api.types.basicGroupFullInfo`):
            New full information about the group

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateBasicGroupFullInfo"

    def __init__(self, basic_group_id, basic_group_full_info, **kwargs):
        
        self.basic_group_id = basic_group_id  # int
        self.basic_group_full_info = basic_group_full_info  # BasicGroupFullInfo

    @staticmethod
    def read(q: dict, *args) -> "UpdateBasicGroupFullInfo":
        basic_group_id = q.get('basic_group_id')
        basic_group_full_info = Object.read(q.get('basic_group_full_info'))
        return UpdateBasicGroupFullInfo(basic_group_id, basic_group_full_info)
