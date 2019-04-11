

from ..utils import Object


class GetSupergroupMembers(Object):
    """
    Returns information about members or banned users in a supergroup or channel. Can be used only if SupergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters 

    Attributes:
        ID (:obj:`str`): ``GetSupergroupMembers``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel
        filter (:class:`telegram.api.types.SupergroupMembersFilter`):
            The type of users to returnBy default, supergroupMembersRecent 
        offset (:obj:`int`):
            Number of users to skip 
        limit (:obj:`int`):
            The maximum number of users be returned; up to 200

    Returns:
        ChatMembers

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSupergroupMembers"

    def __init__(self, supergroup_id, filter, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.filter = filter  # SupergroupMembersFilter
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetSupergroupMembers":
        supergroup_id = q.get('supergroup_id')
        filter = Object.read(q.get('filter'))
        offset = q.get('offset')
        limit = q.get('limit')
        return GetSupergroupMembers(supergroup_id, filter, offset, limit)
