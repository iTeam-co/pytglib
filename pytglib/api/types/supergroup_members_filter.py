

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
    def read(q: dict, *args) -> "SupergroupMembersFilterMention or SupergroupMembersFilterRestricted or SupergroupMembersFilterSearch or SupergroupMembersFilterContacts or SupergroupMembersFilterAdministrators or SupergroupMembersFilterBanned or SupergroupMembersFilterRecent or SupergroupMembersFilterBots":
        if q.get("@type"):
            return Object.read(q)
        return SupergroupMembersFilter()
