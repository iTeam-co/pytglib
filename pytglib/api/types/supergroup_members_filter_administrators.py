

from ..utils import Object


class SupergroupMembersFilterAdministrators(Object):
    """
    Returns the owner and administrators

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterAdministrators``

    No parameters required.

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterAdministrators"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterAdministrators":
        
        return SupergroupMembersFilterAdministrators()
