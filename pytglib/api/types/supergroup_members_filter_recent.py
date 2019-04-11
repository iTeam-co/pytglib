

from ..utils import Object


class SupergroupMembersFilterRecent(Object):
    """
    Returns recently active users in reverse chronological order

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterRecent``

    No parameters required.

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterRecent"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterRecent":
        
        return SupergroupMembersFilterRecent()
