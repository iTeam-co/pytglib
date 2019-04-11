

from ..utils import Object


class SupergroupMembersFilterSearch(Object):
    """
    Used to search for supergroup or channel members via a (string) query 

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterSearch``

    Args:
        query (:obj:`str`):
            Query to search for

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterSearch"

    def __init__(self, query, **kwargs):
        
        self.query = query  # str

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterSearch":
        query = q.get('query')
        return SupergroupMembersFilterSearch(query)
