

from ..utils import Object


class SupergroupMembersFilterBots(Object):
    """
    Returns bot members of the supergroup or channel

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterBots``

    No parameters required.

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterBots"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterBots":
        
        return SupergroupMembersFilterBots()
