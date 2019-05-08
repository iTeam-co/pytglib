

from ..utils import Object


class SupergroupMembersFilter(Object):
    """
    Specifies the kind of chat members to return in getSupergroupMembers

    No parameters required.
    """
    ID = "supergroupMembersFilter"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterRestricted or SupergroupMembersFilterSearch or SupergroupMembersFilterRecent or SupergroupMembersFilterAdministrators or SupergroupMembersFilterBots or SupergroupMembersFilterBanned":
        if q.get("@type"):
            return Object.read(q)
        return SupergroupMembersFilter()
