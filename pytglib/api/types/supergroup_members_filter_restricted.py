

from ..utils import Object


class SupergroupMembersFilterRestricted(Object):
    """
    Returns restricted supergroup members; can be used only by administrators 

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterRestricted``

    Args:
        query (:obj:`str`):
            Query to search for

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterRestricted"

    def __init__(self, query, **kwargs):
        
        self.query = query  # str

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterRestricted":
        query = q.get('query')
        return SupergroupMembersFilterRestricted(query)
